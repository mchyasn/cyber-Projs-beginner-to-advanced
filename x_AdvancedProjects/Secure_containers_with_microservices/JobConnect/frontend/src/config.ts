import * as process from "node:process";

export default {
    imagesUrl: import.meta.env.VITE_IMAGES_URL || 'http://localhost:3002',
    chatBackend: import.meta.env.VITE_CHAT_URL || 'http://localhost:3001',
    backendUrl: import.meta.env.VITE_BACKEND_URL || 'http://localhost:3000',
    keycloak: {
        baseUrl: import.meta.env.VITE_KEYCLOAK_BASE_URL,
        realm: import.meta.env.VITE_KEYCLOAK_REALM,
        clientId: import.meta.env.VITE_KEYCLOAK_CLIENT_ID,
        redirectUri: location.origin + '/login-callback',
    }
}