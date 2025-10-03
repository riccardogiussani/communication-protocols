from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = '127.0.0.1'
PORT = 8080

Handler = SimpleHTTPRequestHandler

# Create the server instance
httpd = HTTPServer((HOST, PORT), Handler)

print(f"HTTP server listening on http://{HOST}:{PORT}")

# Start the server and serve requests indefinitely
httpd.serve_forever()