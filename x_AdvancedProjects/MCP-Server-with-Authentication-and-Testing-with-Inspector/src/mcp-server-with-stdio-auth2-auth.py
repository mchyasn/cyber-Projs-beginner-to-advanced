# src\mcp-server-with-stdio-auth2-auth.py

"""
MCP Server with OAuth2 Authentication (via token introspection)
"""

import asyncio
import json
import os
import sys
import traceback
import requests
from typing import Any, Dict, Optional, Set
from dataclasses import dataclass

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
    ListToolsResult,
    ErrorData,
    INVALID_REQUEST,
    INVALID_PARAMS,
    METHOD_NOT_FOUND,
)
from mcp.shared.exceptions import McpError

@dataclass
class RequestContext:
    token: Optional[str] = None
    is_authenticated: bool = False
    user_id: Optional[str] = None
    permissions: Set[str] = None


class OAuth2AuthenticatedServer:
    def __init__(self):
        # OAuth2 configuration
        self.introspection_url = os.getenv(
            "OAUTH2_INTROSPECTION_URL", 
            "https://your-oauth-provider.com/oauth2/introspect"
        )
        self.client_id = os.getenv("OAUTH2_CLIENT_ID", "mcp-client")
        self.client_secret = os.getenv("OAUTH2_CLIENT_SECRET", "change-me")
        
        self.server = Server("oauth2-authenticated-server")
        self.setup_handlers()

    def verify_oauth2_token(self, token: str) -> Dict[str, Any]:
        """
        Validate OAuth2 access token using the provider's introspection endpoint.
        """
        try:
            response = requests.post(
                self.introspection_url,
                data={"token": token},
                auth=(self.client_id, self.client_secret),
                timeout=5
            )
            data = response.json()
            if not data.get("active"):
                raise McpError(
                    ErrorData(
                        code=INVALID_REQUEST,
                        message="OAuth2 token is inactive or invalid"
                    )
                )
            return data
        except Exception as e:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"OAuth2 token verification failed: {str(e)}"
                )
            )

    def extract_oauth2_token(self, arguments: Dict[str, Any]) -> Optional[str]:
        """Extract OAuth2 token from request arguments."""
        try:
            if "_access_token" in arguments:
                return arguments["_access_token"]
            if "_auth" in arguments and "token" in arguments["_auth"]:
                return arguments["_auth"]["token"]
            if "_meta" in arguments and "access_token" in arguments["_meta"]:
                return arguments["_meta"]["access_token"]
            # fallback to environment
            return os.getenv("MCP_OAUTH2_TOKEN")
        except Exception as e:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"Error extracting OAuth2 token: {str(e)}"
                )
            )

    def authenticate_request(self, arguments: Dict[str, Any]) -> RequestContext:
        """Authenticate request using OAuth2 token"""
        try:
            token = self.extract_oauth2_token(arguments)

            if not token:
                raise McpError(
                    ErrorData(
                        code=INVALID_REQUEST,
                        message="Missing OAuth2 access token."
                    )
                )
            
            payload = self.verify_oauth2_token(token)
            context = RequestContext(
                token=token,
                is_authenticated=True,
                user_id=payload.get("username") or payload.get("sub"),
                permissions=set(payload.get("scope", "").split())
            )
            return context
        except McpError:
            raise
        except Exception as e:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"Unexpected authentication error: {str(e)}"
                )
            )

    def check_permission(self, context: RequestContext, required_permission: str) -> bool:
        try:
            return required_permission in (context.permissions or set())
        except Exception:
            return False

    def setup_handlers(self):
        @self.server.list_tools()
        async def list_tools() -> ListToolsResult:
            try:
                tools = [
                    Tool(
                        name="echo",
                        description="Echo a simple message (requires 'read' scope)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "message": {"type": "string"},
                                "_access_token": {"type": "string", "description": "OAuth2 access token"}
                            },
                            "required": ["message"]
                        },
                    ),
                    Tool(
                        name="secure_action",
                        description="Perform a secure action (requires 'write' scope)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "action": {"type": "string"},
                                "_access_token": {"type": "string", "description": "OAuth2 access token"}
                            },
                            "required": ["action"]
                        },
                    ),
                    Tool(
                        name="admin_action",
                        description="Perform an admin action (requires 'admin' scope)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "command": {"type": "string"},
                                "_access_token": {"type": "string", "description": "OAuth2 access token"}
                            },
                            "required": ["command"]
                        },
                    )
                ]
                return tools
            except Exception as e:
                print("ERROR in list_tools handler:", file=sys.stderr)
                traceback.print_exc()
                raise McpError(
                    ErrorData(
                        code=INVALID_REQUEST,
                        message=f"list_tools error: {str(e)}"
                    )
                )

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
            print(f"DEBUG: call_tool received name={name}", file=sys.stderr)
            try:
                # All tools require an access token
                context = self.authenticate_request(arguments)

                if name == "echo":
                    if not self.check_permission(context, "read"):
                        raise McpError(
                            ErrorData(
                                code=INVALID_REQUEST,
                                message="Insufficient scope: 'read' required."
                            )
                        )
                    message = arguments.get("message", "")
                    return [
                        TextContent(
                            type="text",
                            text=f"Echo (authenticated as {context.user_id}): {message}"
                        )
                    ]
                
                elif name == "secure_action":
                    if not self.check_permission(context, "write"):
                        raise McpError(
                            ErrorData(
                                code=INVALID_REQUEST,
                                message="Insufficient scope: 'write' required."
                            )
                        )
                    action = arguments.get("action", "")
                    return [
                        TextContent(
                            type="text",
                            text=f"Secure action '{action}' executed by {context.user_id}"
                        )
                    ]
                
                elif name == "admin_action":
                    if not self.check_permission(context, "admin"):
                        raise McpError(
                            ErrorData(
                                code=INVALID_REQUEST,
                                message="Insufficient scope: 'admin' required."
                            )
                        )
                    command = arguments.get("command", "")
                    return [
                        TextContent(
                            type="text",
                            text=f"Admin command '{command}' executed by administrator {context.user_id}"
                        )
                    ]
                
                else:
                    raise McpError(
                        ErrorData(
                            code=METHOD_NOT_FOUND,
                            message=f"Unknown tool: {name}"
                        )
                    )
            except McpError:
                raise
            except Exception as e:
                print("ERROR in call_tool handler:", file=sys.stderr)
                traceback.print_exc()
                raise McpError(
                    ErrorData(
                        code=INVALID_REQUEST,
                        message=f"call_tool error: {str(e)}"
                    )
                )


async def main():
    server_instance = OAuth2AuthenticatedServer()
    print("OAuth2 Authenticated MCP Server starting...", file=sys.stderr)
    print(f"  - Introspection URL: {server_instance.introspection_url}", file=sys.stderr)
    print("  - Client ID:", server_instance.client_id, file=sys.stderr)
    print("\nUsage:", file=sys.stderr)
    print("1. First get an OAuth2 access token from your provider", file=sys.stderr)
    print("2. Use the token in '_access_token' field for calls", file=sys.stderr)

    try:
        async with stdio_server() as (read_stream, write_stream):
            await server_instance.server.run(
                read_stream,
                write_stream,
                server_instance.server.create_initialization_options()
            )
    except Exception as e:
        print("MAIN SERVER ERROR:", file=sys.stderr)
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

