from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = '127.0.0.1'

Handler = SimpleHTTPRequestHandler

# Create the server instance
httpd = HTTPServer((HOST, PORT), Handler)

print(f"Server listening on http://{HOST}:{PORT}")

# Start the server and serve requests indefinitely
httpd.serve_forever()