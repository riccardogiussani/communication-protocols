from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

HOST = '127.0.0.1'
PORT = 8080

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        route = parsed_path.path

        if route == "/":
            # Construct response to send back
            response = ""
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        route = parsed_path.path

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode()
        params = urllib.parse.parse_qs(post_data)

        if route == "/my_api_endpoint":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            if(params.get("message") is None):
                self.wfile.write(b"Did not receive any message.")
            else:
                message = params.get("message")
                self.wfile.write(f"Received: {message}".encode())
        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"HTTP server listening on http://{HOST}:{PORT}")
    httpd.serve_forever()
