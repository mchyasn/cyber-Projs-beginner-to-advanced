import http.server
import ssl
import os

# Serve only the 'web' folder
web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

server_address = ('0.0.0.0', 8443)
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(server_address, handler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="../certs/cert.pem", keyfile="../certs/key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("🔐 HTTPS Server running on https://localhost:8443")
httpd.serve_forever()
