# src\mcp-server-with-stdio-api-key-auth.py

"""
MCP Server with API Key Authentication (robust debug handling)
"""

import asyncio
import json
import os
import sys
import traceback
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

import logging
from config.app_settings import AppSettings
from config.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@dataclass
class RequestContext:
    api_key: Optional[str] = None
    is_authenticated: bool = False


class APIKeyAuthenticatedServer:
    def __init__(self):
        self.valid_api_keys: Set[str] = {
            "sk-1234567890abcdef",
            "sk-abcdef1234567890",
            "sk-test123456789",
        }
        self.server = Server("api-key-authenticated-server")
        self.setup_handlers()

    def extract_api_key(self, arguments: Dict[str, Any]) -> Optional[str]:
        if "_api_key" in arguments:
            return arguments["_api_key"]
        if "_meta" in arguments and "api_key" in arguments["_meta"]:
            return arguments["_meta"]["api_key"]
        return os.getenv("MCP_API_KEY")

    def is_valid_api_key(self, api_key: Optional[str]) -> bool:
        return api_key in self.valid_api_keys if api_key else False

    def authenticate_request(self, arguments: Dict[str, Any]) -> RequestContext:
        api_key = self.extract_api_key(arguments)
        context = RequestContext(
            api_key=api_key,
            is_authenticated=self.is_valid_api_key(api_key),
        )
        if not context.is_authenticated:
            raise McpError(
                ErrorData(
                    code=INVALID_REQUEST,
                    message="Invalid or missing API key."
                )
            )
        return context

    def setup_handlers(self):
        @self.server.list_tools()
        async def list_tools() -> ListToolsResult:
            try:
                tools = [
                    Tool(
                        name="echo",
                        description="Echo a simple message (no authentication required)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "message": {"type": "string"}
                            },
                            "required": ["message"]
                        },
                    )
                ]
                return tools
            except Exception as e:
                logger.exception("list_tools failed")
                raise McpError(
                    ErrorData(
                        code=INVALID_REQUEST,
                        message="An internal error occurred while listing tools."
                    )
                )

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
            logger.debug(f"call_tool received name={name}, args={arguments}")
            try:
                # Validate the tool name
                if name not in {"echo"}:
                    raise McpError(
                        ErrorData(
                            code=METHOD_NOT_FOUND,
                            message=f"Tool '{name}' not found."
                        )
                    )
                # Authenticate if needed
                _ = self.authenticate_request(arguments)

                if name == "echo":
                    message = arguments.get("message", "")
                    return [
                        TextContent(type="text", text=f"Echo: {message}")
                    ]
                # fallback: should not happen
                raise McpError(
                    ErrorData(
                        code=METHOD_NOT_FOUND,
                        message=f"Tool handler for '{name}' not implemented."
                    )
                )
            except McpError:
                raise
            except Exception as e:
                logger.exception("call_tool encountered unexpected error")
                raise McpError(
                    ErrorData(
                        code=INVALID_REQUEST,
                        message="An internal server error occurred while executing the tool."
                    )
                )


async def main():
    server_instance = APIKeyAuthenticatedServer()
    logger.info("API Key Authenticated MCP Server starting...")
    for key in server_instance.valid_api_keys:
        logger.info(f"  - valid key prefix: {key[:8]}...")

    try:
        async with stdio_server() as (read_stream, write_stream):
            await server_instance.server.run(
                read_stream,
                write_stream,
                server_instance.server.create_initialization_options()
            )
    except Exception:
        logger.exception("MCP Server failed to start.")
        print("MAIN SERVER ERROR:", file=sys.stderr)
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())



# MCP Inspector (on Bash): $ npx @modelcontextprotocol/inspector uv -e MCP_API_KEY=sk-1234567890abcdef --directory 'D:/My Study/AI/GitHub ahmad-act/MCP-Server-with-Authentication-and-Testing-with-Inspector/src' run mcp-server-with-stdio-api-key-auth.py --debug
# Live: http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=xxxxxxxxxxx
# Command: uv
# Arguments: --directory "D:/My Study/AI/GitHub ahmad-act/MCP-Server-with-Authentication-and-Testing-with-Inspector/src" run mcp-server-with-stdio-auth.py --debug
# Env: MCP_API_KEY=sk-1234567890abcdef"