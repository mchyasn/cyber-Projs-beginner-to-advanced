import http.server
import ssl

server_address = ('0.0.0.0', 8443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile="certs/key.pem",
    certfile="certs/cert.pem",
    server_side=True
)

print("🔐 HTTPS Server running on https://localhost:8443")
httpd.serve_forever()
