from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    query_components = parse_qs(urlparse(self.path).query)
    if (query_components):
      name = query_components.get("name")[0]
      message = query_components.get("message")[0]
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(f"Hello {name}! {message}!".encode('ascii', errors='xmlcharrefreplace'))
    else:
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(f"Вы не передали параметры!".encode('ascii', errors='xmlcharrefreplace'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f"Starting httpd server on port {port}")
  httpd.serve_forever()


if __name__ == "__main__":
  run()
