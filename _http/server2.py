from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        route = parsed_path.path

        if route == "/":
            self.respond_text("Welcome to the Python HTTP server!")
        elif route == "/greet":
            self.respond_text("Hello World from the greeting endpoint!")
        elif route == "/json":
            data = {"message": "Hello from JSON endpoint", "status": "ok"}
            self.respond_json(data)
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        route = parsed_path.path

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode()
        params = urllib.parse.parse_qs(post_data)

        if route == "/echo":
            message = params.get("message", ["(no message)"])[0]
            self.respond_text(f"Echo: {message}")
        elif route == "/sum":
            try:
                a = int(params.get("a", [0])[0])
                b = int(params.get("b", [0])[0])
                result = {"a": a, "b": b, "sum": a + b}
                self.respond_json(result)
            except ValueError:
                self.send_error(400, "Invalid numbers")
        else:
            self.send_error(404, "Not Found")

    # Helpers
    def respond_text(self, text):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(text.encode())

    def respond_json(self, data):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == "__main__":
    server_address = ("localhost", 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Serving on http://localhost:8080")
    httpd.serve_forever()
