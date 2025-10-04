import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

class VideoHAndler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            file_list = os.listdir(path)
            html = "<html><head><title>Video</title></head><body>"
            html += "<h1>Video</h1>"
            for file in file_list:
                if file.lower().endswith(('.mp4', '.avi', '.mkv', 'webm', 'ogg')):
                    html += f'<div><video width="320" height="240" controls><source src="{file}" type="video/mp4">Your browser does not support the video tag.</video><p>{file}</p></div>'
                
                    html += "</body></html>"
                    encoded = html.encode('utf-8')
                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.send_header("Content-Length", str(len(encoded)))
                    self.end_headers()
                    return self.wfile.write(encoded)
        except Exception as e:
            self.send_error(404, str(e))
            
        httpd = HTTPServer(("0.0.0.0", PORT), VideoHAndler)
        print(f"Serving on port {PORT}")
        httpd.serve_forever()