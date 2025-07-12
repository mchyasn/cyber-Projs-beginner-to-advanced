import { reactive, ref } from 'vue';
import axios from 'axios';
import * as client from 'openid-client';
import {jwtDecode} from "jwt-decode";
import config from "@/config";

const localStorageUtil = {
    get: (key: string) => localStorage.getItem(key),
    set: (key : string, value : string) => localStorage.setItem(key, value),
    remove: (key: string) => localStorage.removeItem(key),
};
// State for auth
const state = reactive({
    accessToken: localStorageUtil.get('access_token') || undefined,
    refreshToken: localStorageUtil.get('refresh_token') || undefined,
    user: localStorageUtil.get('user') ? JSON.parse(<string>localStorageUtil.get('user')) : undefined,
    authenticated: !!localStorageUtil.get('access_token')
});
const error = ref<string | undefined>(undefined);
let codeChallenge: string;
let authConfig: client.Configuration;

export function useAuth() {

    const init = async () => {
        const issuerUri = `${config.keycloak.baseUrl}/realms/${config.keycloak.realm}`;
        authConfig = await client.discovery(
            new URL(issuerUri),
            config.keycloak.clientId!,
            undefined,
            undefined,
            { execute: [client.allowInsecureRequests] } // allow running Keycloak on localhost
        );
    }

    const login = async () => {
        console.log("login");
        /**
         * PKCE: The following MUST be generated for every redirect to the
         * authorization_endpoint. You must store the code_verifier and state in the
         * end-user session such that it can be recovered as the user gets redirected
         * from the authorization server back to your application.
         */
        localStorageUtil.set('code_verifier', client.randomPKCECodeVerifier())
        codeChallenge = await client.calculatePKCECodeChallenge(<string>localStorageUtil.get('code_verifier'))

        let parameters: Record<string, string> = {
            redirect_uri: config.keycloak.redirectUri,
            code_challenge: codeChallenge,
            code_challenge_method: 'S256',
        }

        localStorageUtil.set('state', client.randomState())
        parameters.state = <string>localStorageUtil.get('state')

        let redirectTo: URL = client.buildAuthorizationUrl(authConfig, parameters)
        window.location.href = redirectTo.href; // Redirect to Keycloak login page
    };

    /**
     * Handle the callback after login
     */
    const handleCallback = async (callbackUrl: string) => {
        let tokens: client.TokenEndpointResponse = await client.authorizationCodeGrant(
            authConfig,
            new URL(callbackUrl),
            {
                pkceCodeVerifier: <string>localStorageUtil.get('code_verifier'),
                expectedState: <string>localStorageUtil.get('state'),
            },
        )

        state.authenticated = true;
        state.accessToken = tokens.access_token;
        state.refreshToken = tokens.refresh_token;
        state.user = jwtDecode(tokens.access_token);

        localStorageUtil.set('access_token', tokens.access_token);
        localStorageUtil.set('refresh_token', tokens.refresh_token ?? "");
        localStorageUtil.set('user', JSON.stringify(state.user));


    };


    /**
     * Make an authenticated request to the backend
     */
    const authorizedRequest = async (endpoint: string, method: string, options = {}) => {
        await refreshToken()
        if (!state.accessToken) {
            error.value = 'Not authenticated';
            throw new Error(error.value);
        }

        const response = await axios({
            url: `${endpoint}`,
            headers: {
                Authorization: `Bearer ${state.accessToken}`,
            },
            method: method,
            ...options,
        });
        return response.data;
    };

    const refreshToken = async () => {
        const refreshToken = state.refreshToken;
        if (!refreshToken) {
            console.error("No refresh token available.");
            cleanLocalStorage()
            return undefined;
        }

        try {
            const response = await axios.post(
                `${config.keycloak.baseUrl}/realms/${config.keycloak.realm}/protocol/openid-connect/token`,
                new URLSearchParams({
                    client_id: config.keycloak.clientId!,
                    grant_type: 'refresh_token',
                    refresh_token: refreshToken,
                }),
                {
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                }
        );

            const newAccessToken = response.data.access_token;
            const newRefreshToken = response.data.refresh_token;
            
            state.accessToken = newAccessToken;
            state.refreshToken = newRefreshToken;
            state.user = jwtDecode(newAccessToken);

            localStorageUtil.set('access_token', newAccessToken);
            localStorageUtil.set('refresh_token', newRefreshToken);
            localStorageUtil.set('user', JSON.stringify(state.user));

            return newAccessToken;
        } catch (err) {
            console.error("Failed to refresh token:", err);
            cleanLocalStorage()
            return undefined;
        }
    };

    const logout = () => {
        cleanLocalStorage()
        window.location.href = `${config.keycloak.baseUrl}/realms/${config.keycloak.realm}/protocol/openid-connect/logout?redirect_uri=${encodeURIComponent(location.origin)}`;
    };

    const cleanLocalStorage = () => {
        state.authenticated = false;
        state.accessToken = undefined;
        state.refreshToken = undefined;
        state.user = undefined;
        localStorageUtil.remove('access_token');
        localStorageUtil.remove('refresh_token');
        localStorageUtil.remove('user');
        localStorageUtil.remove('state');
        localStorageUtil.remove('code_verifier')
    }
    const unauthorizedRequest = async (endpoint: string, method: string, options = {}) => {
        const response = await axios({
            url: `${endpoint}`,
            method: method,
            ...options,
        });
        return response.data;
    };

    const getUsername = () => {
        return state.user?.['preferred_username']
    };

    const getUserRoles = () => {
        return state.user?.['resource_access']?.[config.keycloak.clientId]?.roles ?? []
    }

    const getUserEmail = () => {
        return state.user?.['email']
    }

    return {
        state,
        error,
        init,
        login,
        handleCallback,
        authorizedRequest,
        unauthorizedRequest,
        getUsername,
        getUserRoles,
        getUserEmail,
        logout
    };
}
