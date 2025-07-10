#  MCP Server with Authentication and Testing with Inspector

This project implements a Model Context Protocol (MCP) server with two authentication mechanisms: API Key Authentication and JWT (JSON Web Token) Authentication. It provides a robust framework for handling authenticated requests with comprehensive error handling and logging, suitable for production environments. The server supports tools like `echo`, `login`, `secure_action`, and `admin_action`, with authentication enforced where required.

#  Table of Contents

1. [ Project Overview](#-mcp-server-with-authentication-and-testing-with-inspector)

2. [ Purpose](#-purpose)

3. [ Features](#-features)

4. [ Project Structure](#-project-structure)

5. [ Prerequisites](#-prerequisites)

6. [ Installation](#-installation)
   - [ Clone the Repository](#-clone-the-repository)
   - [ Set Up a Virtual Environment](#-set-up-a-virtual-environment-recommended)
   - [ Install Dependencies](#-install-dependencies)

7. [ Packages](#-packages)

8. [ Usage](#-usage)
   - [ MCP Server with Stdio and API Key](#-mcp-server-with-stdio-and-api-key-mcp-server-with-stdio-api-key-authpy)
     - [ Run the MCP Server](#️-run-the-mcp-server)
     - [ Run the MCP Inspector](#-run-the-mcp-inspector)
     - [ Open the MCP Inspector](#-open-the-mcp-inspector)
     - [ Using the MCP Inspector](#-using-the-mcp-inspector)
   - [ MCP Server with Stdio and JWT](#-mcp-server-with-stdio-and-jwt-mcp-server-with-stdio-jwt-key-authpy)
     - [ Run the MCP Server](#️-run-the-mcp-server-1)
     - [ Run the MCP Inspector](#-run-the-mcp-inspector-1)
     - [ Open the MCP Inspector](#-open-the-mcp-inspector-1)
     - [ Using the MCP Inspector](#-using-the-mcp-inspector-1)
   - [ MCP Server with Stdio and Auth2 (To Do)](#-mcp-server-with-stdio-and-auth2-mcp-server-with-stdio-auth2-authpy)

9. [ Workflow](#-workflow)

10. [ Troubleshooting](#-troubleshooting)
   - [ Invalid API Key](#-invalid-api-key)
   - [ Invalid JWT Token](#-invalid-jwt-token)
   - [ Permission Errors](#-permission-errors)
   - [ Log Files](#-log-files)

##  Purpose

The purpose of this project is to demonstrate secure MCP server implementations with two distinct authentication methods:
-  **API Key Authentication**: Validates requests using predefined API keys.
-  **JWT Authentication**: Uses JSON Web Tokens for user authentication and permission-based access control.

This project is designed for developers who need a secure, scalable, and extensible MCP server with robust debugging and logging capabilities.

##  Features

-  **API Key Authentication**:
  - Validates requests using a set of predefined API keys.
  - Supports key extraction from arguments, metadata, or environment variables.
  - Simple `echo` tool for demonstration.

-  **JWT Authentication**:
  - Supports user authentication via username/password to generate JWT tokens.
  - Enforces permission-based access control (`read`, `write`, `admin`).
  - Includes tools: `login`, `echo`, `secure_action`, and `admin_action`.
  - Configurable token expiry (default: 24 hours).
  - Token extraction from arguments, metadata, or environment variables.

- **Robust Error Handling**:
  - Custom `McpError` for consistent error responses.
  - Detailed logging of errors and server events.

-  **Logging**:
  - Configurable logging to both console and rotating log files.
  - Log rotation based on file size (5MB, with 5 backups).
  - Automatic cleanup of old log files based on age.

-  **MCP Inspector Integration**:
  - Compatible with MCP Inspector for testing and debugging.
  - Supports debugging via `--debug` flag.

##  Prerequisites

- **Python**: Version 3.13 or higher
- **uv**: Used for managing Python virtual environments
- **Node.js**: Required for running MCP Inspector
- **NPM**: Required to run MCP Inspector
- **Operating System**: Windows, macOS, or Linux

##  Installation

1.  **Clone the Repository**:
   ```bash
   git clone https://github.com/ahmad-act/MCP-Server-with-Authentication-and-Testing-with-Inspector.git
   cd MCP-Server-with-Authentication-and-Testing-with-Inspector
   ```

2.  **Set Up a Virtual Environment** (recommended):
   ```bash
   uv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3.  **Install Dependencies**:
   ```bash
   uv sync
   ```
---

##  Packages

The following Python packages are required:

```plaintext
mcp[cli]>=1.10.1
PyJWT>=2.8.0
python-dotenv>=1.0.0
```

 Install them using:

```bash
uv add mcp[cli] PyJWT python-dotenv
```

##  Usage

###  MCP Server with Stdio and API Key (`mcp-server-with-stdio-api-key-auth.py`)

####  **Run the MCP Server**:

 *You do not need to manually run the MCP server for stdio transport. MCP Inspector runs the MCP Server for stdio transport.*

####  **Run the MCP Inspector**:

The `stdio` server is typically launched by the MCP Inspector, not manually. Run the Inspector with the following command, add `-e` environment variable and adjusting the `--directory` path to your `src/` directory:

```bash
npx @modelcontextprotocol/inspector uv -e MCP_API_KEY=sk-1234567890abcdef --directory '<your-src-directory>/src' run mcp-server-with-stdio-api-key-auth.py --debug
```

![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/1.png)

####  **Open the MCP Inspector**:

Open the link `http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=XXXXXXXXXXXXXXXXXX` with its token in your browser:

![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/0.png)

####  **Using the MCP Inspector**

1. After running the above command, the Inspector will start and automatically connect to the `stdio`-based server.
2. In the Inspector UI (`http://127.0.0.1:6274`), inspect the available tools (e.g., `echo`).
3. Test the `echo` tool:

   - **Input**:

   ```json
   {
     "method": "call_tool",
     "params": {
       "name": "echo",
       "arguments": {
         "message": "test",
         "_api_key": "sk-1234567890abcdef"
       }
     }
   }
   ```

   **Expected Response**:

   ```json
   {
     "result": [
       {
         "type": "text",
         "text": "Echo: test"
       }
     ]
   }
   ```
![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/6.png)
![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/7.png)
![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/9.png)

###  MCP Server with Stdio and API Key (`mcp-server-with-stdio-jwt-key-auth.py`)

####  **Run the MCP Server**:

 *You do not need to manually run the MCP server for stdio transport. MCP Inspector will launch the server automatically.*

####  **Run the MCP Inspector**:

The `stdio` server is typically launched by the MCP Inspector, not manually. Run the Inspector with the following command, adjusting the `--directory` path to your `src/` directory:

```bash
npx @modelcontextprotocol/inspector uv --directory '<your-src-directory>\src' run mcp-server-with-stdio-jwt-key-auth.py --debug
```

![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/1.png)

####  **Open the MCP Inspector**:

Open the link http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=XXXXXXXXXXXXXXXXXX with its token in your browser:

![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/4.png)

####  **Using the MCP Inspector**

1. After running the above command, the Inspector will start and automatically connect to the `stdio`-based server.

2. **Usage Flow**:
   - **Step 1: Login to Get JWT Token**:
     ```json
     {
       "method": "call_tool",
       "params": {
         "name": "login",
         "arguments": {
           "username": "user1",
           "password": "password123"
         }
       }
     }
     ```
     **Response**:
     ```json
     {
       "result": [
         {
           "type": "text",
           "text": "Login successful! JWT Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
         }
       ]
     }
     ```

   - **Step 2: Use JWT Token for Authenticated Requests**:
     ```json
     {
       "method": "call_tool",
       "params": {
         "name": "echo",
         "arguments": {
           "message": "test",
           "_jwt_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
         }
       }
     }
     ```
     **Response**:
     ```json
     {
       "result": [
         {
           "type": "text",
           "text": "Echo (authenticated as user1): test"
         }
       ]
     }
     ```
![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/6.png)
![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/7.png)
![MCP Server Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/x_AdvancedProjects/MCP-Server-with-Authentication-and-Testing-with-Inspector/doc/8.png)

###  MCP Server with Stdio and Auth2 (`mcp-server-with-stdio-auth2-auth.py`)

🚧 **To Do**

---

##  Workflow

1.  **API Key Authentication**:
   - The server checks for a valid API key in the request arguments, metadata, or environment variables.
   - If valid, the request is processed; otherwise, an error is returned.
   - The `echo` tool demonstrates basic functionality.

2.  **JWT Authentication**:
   - Users first call the `login` tool with valid credentials to obtain a JWT token.
   - The token is used in subsequent requests for tools like `echo`, `secure_action`, or `admin_action`.
   - Permissions (`read`, `write`, `admin`) are checked for each tool.
   - Tokens expire after 24 hours (configurable).

3.  **Logging**:
   - Logs are written to both the console and a rotating log file in the `logs` directory.
   - Old log files are cleaned up based on a specified retention period.

4.  **Testing with MCP Inspector**:
   - Use MCP Inspector to interact with the server via a web interface.
   - Debug mode (`--debug`) provides detailed output for troubleshooting.

##  Troubleshooting

-  **Invalid API Key**:
  - Ensure the API key is one of: `sk-1234567890abcdef`, `sk-abcdef1234567890`, `sk-test123456789`.
  - Check environment variable `MCP_API_KEY` or request arguments.

-  **Invalid JWT Token**:
  - Verify the token is not expired (valid for 24 hours).
  - Ensure the correct `JWT_SECRET` is set.
  - Check username/password for `login` tool.

-  **Permission Errors**:
  - Ensure the user has the required permissions (`read`, `write`, or `admin`) for the requested tool.

-  **Log Files**:
  - Check the `logs` directory for detailed error messages.
  - Logs are named in the format `YYYYMM.log`.
