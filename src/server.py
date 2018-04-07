from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from sys import argv
from cowpy import cow
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)
        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'''
                <!DOCTYPE html>
                <html>
                <head>
                  <title> cowsay </title>
                  </head>
                  <body>
                    <header>
                     <nav>
                       <ul>
                         <li><a href="/cowsay">cowsay</a></li>
                       </ul>
                     </nav>
                    </header>
                    <main>
                      <!-- project description -->
                    </main>
                </body>
                </html>
            ''')
            return
        elif parsed_path.path == '/cowsay':
            self.send_response(200)
            self.end_headers()
            pick = cow.Turtle()
            msg = pick.milk("Too Quick My Guy. Head Back Home.")
            self.wfile.write(str.encode(msg))

        elif parsed_path.path == '/cow':
            try:
                text = json.loads(parsed_qs['msg'][0])
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'KeyError')
                return

            self.send_response(200)
            self.end_headers()
            pick = cow.Turtle()
            msg = pick.milk(text)
            self.wfile.write(str.encode(msg))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404: Page Not Found.')
            return

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.send_response_only()


def create_server():
    return HTTPServer(('127.0.0.1', 3001), SimpleHTTPRequestHandler)


def main():
    server = create_server()
    try:
        print('Starting Server on port:', 3001)
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    main()
