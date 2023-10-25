import http.server
import socketserver
import webbrowser

port = 80
adresse = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adresse, handler)

print(f"Server started on port {port}")
print(f"Server address: http://localhost:{port}/HTML/index.html")l)

httpd.serve_forever()
