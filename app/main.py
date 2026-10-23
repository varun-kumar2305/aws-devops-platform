from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class AppHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({"status": "ok"}).encode()
            )

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({
                    "message": "AWS DevOps Platform is running!"
                }).encode()
            )

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({"error": "Not found"}).encode()
            )


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), AppHandler)
    print("Application running on port 8000...")
    server.serve_forever()
