#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8765
DIRECTORY = "/Users/yue/Projects/jianli"

class UTF8HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def guess_type(self, path):
        base, ext = os.path.splitext(path)
        if ext.lower() in (".md", ".markdown"):
            return "text/markdown; charset=utf-8"
        if ext.lower() in (".html", ".htm"):
            return "text/html; charset=utf-8"
        if ext.lower() in (".js",):
            return "application/javascript; charset=utf-8"
        if ext.lower() in (".css",):
            return "text/css; charset=utf-8"
        if ext.lower() in (".txt", ".json", ".yaml", ".yml"):
            return "text/plain; charset=utf-8"
        ctype = super().guess_type(path)
        if ctype and ctype.startswith("text/") and "charset=" not in ctype:
            return f"{ctype}; charset=utf-8"
        return ctype

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    with ReusableTCPServer(("", PORT), UTF8HTTPRequestHandler) as httpd:
        print(f"Serving UTF-8 HTTP on port {PORT} from {DIRECTORY}...")
        httpd.serve_forever()
