import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

class VideoHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            file_list = sorted(os.listdir(path))
            html = """
            <html>
            <head>
                <title>Video Gallery</title>
                <style>
                    body { font-family: Arial; padding: 20px; background: #f0f0f0; }
                    h2 { text-align: center; }
                    .video-container { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }
                    .video-item { background: white; padding: 10px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
                    video { display: block; margin: auto; }
                    p { text-align: center; margin-top: 5px; }
                </style>
            </head>
            <body>
                <h2>Video Gallery</h2>
                <div class="video-container">
            """
            for file in file_list:
                if file.lower().endswith((".mp4", ".webm", ".ogg")):
                    html += f"""
                    <div class="video-item">
                        <video width='320' height='180' controls>
                            <source src='{file}' type='video/mp4'>
                            Your browser does not support the video tag.
                        </video>
                        <p>{file}</p>
                    </div>
                    """
            html += "</div></body></html>"

            encoded = html.encode('utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            return self.wfile.write(encoded)
        except Exception as e:
            self.send_error(404, str(e))

httpd = HTTPServer(("0.0.0.0", PORT), VideoHandler)
print(f"Serving at port {PORT}")
httpd.serve_forever()
