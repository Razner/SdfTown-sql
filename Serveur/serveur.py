import http.server
import socketserver

port = 80
adresse = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adresse, handler)

print(f"Server started on port {port}")
print(f"Server address: http://localhost:{port}")

httpd.serve_forever()
