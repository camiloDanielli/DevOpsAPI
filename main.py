# app_notas_simple.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
from pathlib import Path
import json

PORT = 8000
notas_dir = Path(__file__).parent / "notas"
notas_dir.mkdir(exist_ok=True)

class SimpleHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self._send_json({"mensaje": "API de notas activa"})
        elif self.path == "/list":
            notas = []
            for file in sorted(notas_dir.glob("*.txt")):
                with file.open("r", encoding="utf-8") as f:
                    notas.append({"archivo": file.name, "contenido": f.read()})
            self._send_json({"notas": notas})
        else:
            self._send_json({"error": "Endpoint no encontrado"}, status=404)

    def do_POST(self):
        if self.path.startswith("/add/"):
            # Nombre de la nota desde la URL
            nota_nombre = unquote(self.path[len("/add/"):])

            # Contenido desde el body
            content_length = int(self.headers.get('Content-Length', 0))
            contenido = self.rfile.read(content_length).decode('utf-8')

            # Guardar la nota
            nota_path = notas_dir / f"{nota_nombre}.txt"
            with nota_path.open("w", encoding="utf-8") as f:
                f.write(contenido)

            self._send_json({"mensaje": "Nota agregada", "archivo": nota_path.name})
        else:
            self._send_json({"error": "Endpoint no encontrado"}, status=404)

def run():
    server = HTTPServer(("", PORT), SimpleHandler)
    print(f"Servidor corriendo en http://localhost:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
