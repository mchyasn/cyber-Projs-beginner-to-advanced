# TLS Web Server with HTTPS (Self-Signed Certificate)

Project Goal:
-------------
Deploy a secure HTTPS server locally using a self-signed TLS certificate.
The server should only serve files from a restricted web directory using SSL.

Tools & Tech:
-------------
- Python 3
- openssl (for generating TLS certificates)
- http.server (Python built-in web server)
- ssl module (TLS encryption)
- curl and browser for testing

Step-by-Step Setup:
-------------------

1. Create Folder Structure
--------------------------
mkdir TLSWebServer && cd TLSWebServer
mkdir certs web

2. Generate Self-Signed Certificate
-----------------------------------
```
openssl req -x509 -newkey rsa:2048 -nodes \
-keyout certs/key.pem -out certs/cert.pem \
-days 365 -subj "/CN=localhost"
```
![TLS Web Server Configuration](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TLSWebServer/screenshots/1.png)
3. Create HTML Page to Serve
----------------------------
```
echo "<h1>HTTPS is working!</h1>" > web/index.html
```

4. Create Python HTTPS Server
-----------------------------
Create https_server.py with this content:
```
import http.server
import ssl
import os
```
![TLS Certificate Verification](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TLSWebServer/screenshots/11.png)

# Serve only the web folder
```
web_dir = os.path.join(os.path.dirname(__file__), "web")
os.chdir(web_dir)

server_address = ("0.0.0.0", 8443)
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(server_address, handler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="../certs/cert.pem", keyfile="../certs/key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS Server running on https://localhost:8443")
httpd.serve_forever()
```
![TLS Secure Connection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TLSWebServer/screenshots/2.png)

5. Run the Secure Server
------------------------
```
python3 https_server.py
```

Expected output:
HTTPS Server running on https://localhost:8443
![TLS Handshake Process](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TLSWebServer/screenshots/3.png)

6. Test with curl
-----------------

In a new terminal:

curl -k https://localhost:8443

Output:
```
<h1>HTTPS is working!</h1>
```
![TLS Implementation Complete](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TLSWebServer/screenshots/final.png)

7. Test in Firefox Browser (Optional)
   
-------------------------------------
Open https://localhost:8443
Accept the self-signed certificate warning.

Security Note:
--------------
- This is for local development/testing only.
- For production, use a real TLS certificate from Let\'s Encrypt.

Date: July 6, 2025
  '
);
