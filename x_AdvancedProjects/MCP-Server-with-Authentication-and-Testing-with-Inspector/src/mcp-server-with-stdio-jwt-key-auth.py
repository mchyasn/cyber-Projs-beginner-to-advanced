# src\mcp-server-with-stdio-jwt-key-auth.py

"""
MCP Server with JWT Authentication (robust debug handling)
"""

import asyncio
import json
import os
import sys
import traceback
import jwt
import time
from typing import Any, Dict, Optional, Set
from dataclasses import dataclass
from datetime import datetime, timedelta, UTC

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

import logging
from config.app_settings import AppSettings
from config.logging_config import setup_logging


setup_logging()
logger = logging.getLogger(__name__)

@dataclass
class RequestContext:
    token: Optional[str] = None
    is_authenticated: bool = False
    user_id: Optional[str] = None
    permissions: Set[str] = None


class JWTAuthenticatedServer:
    def __init__(self):
        # JWT configuration
        self.jwt_secret = os.getenv("JWT_SECRET", "your-super-secret-jwt-key-change-this-in-production")
        self.jwt_algorithm = "HS256"
        self.token_expiry_hours = 24
        
        # Valid user credentials (in production, this would be in a database)
        self.valid_users = {
            "user1": {
                "password": "password123",
                "permissions": {"read", "write", "admin"}
            },
            "user2": {
                "password": "secret456",
                "permissions": {"read", "write"}
            },
            "testuser": {
                "password": "test123",
                "permissions": {"read"}
            }
        }
        
        self.server = Server("jwt-authenticated-server")
        self.setup_handlers()

    def generate_jwt_token(self, user_id: str, permissions: Set[str]) -> str:
        """Generate a JWT token for authenticated user"""
        try:
            payload = {
                "user_id": user_id,
                "permissions": list(permissions),
                "iat": datetime.now(UTC),
                "exp": datetime.now(UTC) + timedelta(hours=self.token_expiry_hours),
                "iss": "mcp-jwt-server"
            }
            return jwt.encode(payload, self.jwt_secret, algorithm=self.jwt_algorithm)
        except Exception as e:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"Failed to generate JWT token: {str(e)}"
                )
            )

    def verify_jwt_token(self, token: str) -> Dict[str, Any]:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(
                token,
                self.jwt_secret,
                algorithms=[self.jwt_algorithm],
                options={"verify_exp": True}
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message="Your JWT token has expired. Please re-authenticate."
                )
            )
        except jwt.InvalidTokenError:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message="Invalid JWT token. Please check your token and try again."
                )
            )
        except Exception as e:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"Unexpected error verifying JWT: {str(e)}"
                )
            )

    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        """Authenticate user credentials and return JWT token"""
        try:
            if username in self.valid_users:
                user_data = self.valid_users[username]
                if user_data["password"] == password:
                    return self.generate_jwt_token(username, user_data["permissions"])
            # fail gracefully
            return None
        except Exception as e:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"Failed to authenticate user: {str(e)}"
                )
            )

    def extract_jwt_token(self, arguments: Dict[str, Any]) -> Optional[str]:
        """Extract JWT token from various possible locations"""
        try:
            if "_jwt_token" in arguments:
                return arguments["_jwt_token"]
            if "_auth" in arguments and "token" in arguments["_auth"]:
                return arguments["_auth"]["token"]
            if "_meta" in arguments and "jwt_token" in arguments["_meta"]:
                return arguments["_meta"]["jwt_token"]

            # fallback to environment
            return os.getenv("MCP_JWT_TOKEN")
        except Exception as e:
            # defensively handle bad argument types
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"Error extracting JWT token: {str(e)}"
                )
            )

    def authenticate_request(self, arguments: Dict[str, Any]) -> RequestContext:
        """Authenticate request using JWT token"""
        try:
            token = self.extract_jwt_token(arguments)

            if not token:
                raise McpError(
                    ErrorData(
                        code=INVALID_REQUEST,
                        message="Missing JWT token. Please provide a valid JWT token."
                    )
                )

            payload = self.verify_jwt_token(token)
            context = RequestContext(
                token=token,
                is_authenticated=True,
                user_id=payload.get("user_id"),
                permissions=set(payload.get("permissions", []))
            )
            return context

        except McpError:
            # re-raise so upper layers see consistent McpError
            raise
        except Exception as e:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message=f"An unexpected error occurred during authentication: {str(e)}"
                )
            )

    def check_permission(self, context: RequestContext, required_permission: str) -> bool:
        """
        Check if user has the required permission.
        If any error occurs (e.g., missing context or permissions), return False.
        """
        try:
            return required_permission in (context.permissions or set())
        except Exception as e:
            # Optional: log the error if you have a logger
            # logger.warning(f"Permission check failed: {e}")
            return False

    def setup_handlers(self):
        @self.server.list_tools()
        async def list_tools() -> ListToolsResult:
            try:
                tools = [
                    Tool(
                        name="echo",
                        description="Echo a simple message (requires 'read' permission)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "message": {"type": "string"},
                                "_jwt_token": {"type": "string", "description": "JWT authentication token"}
                            },
                            "required": ["message"]
                        },
                    ),
                    Tool(
                        name="login",
                        description="Authenticate user and get JWT token",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "username": {"type": "string"},
                                "password": {"type": "string"}
                            },
                            "required": ["username", "password"]
                        },
                    ),
                    Tool(
                        name="secure_action",
                        description="Perform a secure action (requires 'write' permission)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "action": {"type": "string"},
                                "_jwt_token": {"type": "string", "description": "JWT authentication token"}
                            },
                            "required": ["action"]
                        },
                    ),
                    Tool(
                        name="admin_action",
                        description="Perform an admin action (requires 'admin' permission)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "command": {"type": "string"},
                                "_jwt_token": {"type": "string", "description": "JWT authentication token"}
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
                        message=f"Error in list_tools: {str(e)}"
                    )
                )

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
            print(f"DEBUG: call_tool received name={name}, type={type(name)}", file=sys.stderr)
            
            try:
                # Handle login separately (no authentication required)
                if name == "login":
                    username = arguments.get("username", "")
                    password = arguments.get("password", "")
                    
                    token = self.authenticate_user(username, password)
                    if token:
                        return [
                            TextContent(
                                type="text", 
                                text=f"Login successful! JWT Token: {token}\n\nThis token will expire in {self.token_expiry_hours} hours.\nUse this token in the '_jwt_token' field for authenticated requests."
                            )
                        ]
                    else:
                        raise McpError(
                            ErrorData(
                                code=INVALID_REQUEST,
                                message="Invalid username or password"
                            )
                        )
                
                # For all other tools, require authentication
                context = self.authenticate_request(arguments)
                
                if name == "echo":
                    if not self.check_permission(context, "read"):
                        raise McpError(
                            ErrorData(
                                code=INVALID_REQUEST,
                                message="Insufficient permissions. 'read' permission required."
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
                                message="Insufficient permissions. 'write' permission required."
                            )
                        )
                    
                    action = arguments.get("action", "")
                    return [
                        TextContent(
                            type="text", 
                            text=f"Secure action '{action}' executed successfully by user {context.user_id}"
                        )
                    ]
                
                elif name == "admin_action":
                    if not self.check_permission(context, "admin"):
                        raise McpError(
                            ErrorData(
                                code=INVALID_REQUEST,
                                message="Insufficient permissions. 'admin' permission required."
                            )
                        )
                    
                    command = arguments.get("command", "")
                    return [
                        TextContent(
                            type="text", 
                            text=f"Admin command '{command}' executed successfully by administrator {context.user_id}"
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
    server_instance = JWTAuthenticatedServer()
    print("JWT Authenticated MCP Server starting...", file=sys.stderr)
    print(f"  - JWT Secret: {server_instance.jwt_secret[:8]}... (truncated)", file=sys.stderr)
    print(f"  - Token expiry: {server_instance.token_expiry_hours} hours", file=sys.stderr)
    print("  - Valid users:", file=sys.stderr)
    for username, data in server_instance.valid_users.items():
        print(f"    * {username}: permissions={list(data['permissions'])}", file=sys.stderr)
    print("\nUsage:", file=sys.stderr)
    print("1. First call 'login' tool with username/password to get JWT token", file=sys.stderr)
    print("2. Use the JWT token in '_jwt_token' field for subsequent authenticated calls", file=sys.stderr)

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


# Installation requirements:
# pip install PyJWT

# MCP Inspector usage:
# $ npx @modelcontextprotocol/inspector uv --directory 'D:/My Study/AI/GitHub ahmad-act/MCP-Server-with-Authentication-and-Testing-with-Inspector/src' run mcp-server-with-stdio-jwt-key-auth.py --debug

# To get the jwt token:
# {
#   "username": "user1", 
#   "password": "password123"
# }
# Environment variables (optional):
# JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
# MCP_JWT_TOKEN=your-jwt-token-here

# Example usage flow:
# 1. Call "login" tool with {"username": "user1", "password": "password123"}
# 2. Copy the returned JWT token
# 3. Use the token in other tools: {"message": "hello", "_jwt_token": "your-jwt-token-here"}