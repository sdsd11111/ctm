import http.server
import socketserver
import os

PORT = 3000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Si la ruta es un directorio, sirve index.html
        if os.path.isdir(self.path.strip('/')):
            self.path = os.path.join(self.path, 'index.html')
        # Si la ruta no tiene extensión, asumimos que es una ruta de la SPA
        elif '.' not in os.path.basename(self.path):
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Cambiar el directorio de trabajo al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor Python iniciado en http://localhost:{PORT}")
    print("Presiona Ctrl+C para detener el servidor")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nDeteniendo el servidor...")
        httpd.server_close()
        print("Servidor detenido.")
