from http.server import HTTPServer, SimpleHTTPRequestHandler


class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        super().do_GET()

    def do_OPTIONS(self):
        print(self.headers)
        self.send_header("Allow", "OPTIONS, GET")
        self.send_header("Access-Control-Allow-Methods", "OPTIONS, GET")
        self.end_headers()

    def end_headers(self):
        self.send_header(
            "Access-Control-Allow-Origin",
            "https://busy-bee-amateurs-ctf-2024.pages.dev",
        )
        self.send_header("Access-Control-Allow-Credentials", "true")
        super().end_headers()


if __name__ == "__main__":
    with HTTPServer(("", 80), RequestHandler) as server:
        server.serve_forever()
