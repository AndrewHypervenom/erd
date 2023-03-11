import socket
import http.server
import matplotlib.pyplot as plt

class SurveyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <html>
            <head><title>Encuesta sobre el cielo</title></head>
            <body>
            <h2>Encuesta sobre el cielo</h2>
            <form method="POST" action="/">
            <p>¿Del 1 al 10 que tanto te gusta el cielo?</p>
            <p><input type="radio" name="respuesta" value="1">1</p>
            <p><input type="radio" name="respuesta" value="2">2</p>
            <p><input type="radio" name="respuesta" value="3">3</p>
            <p><input type="radio" name="respuesta" value="4">4</p>
            <p><input type="radio" name="respuesta" value="5">5</p>
            <p><input type="radio" name="respuesta" value="6">6</p>
            <p><input type="radio" name="respuesta" value="7">7</p>
            <p><input type="radio" name="respuesta" value="8">8</p>
            <p><input type="radio" name="respuesta" value="9">9</p>
            <p><input type="radio" name="respuesta" value="10">10</p>
            <p><input type="submit" value="Enviar"></p>
            </form>
            <form method="POST" action="/stop">
            <p><input type="submit" value="Detener servidor"></p>
            </form>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        elif self.path == '/stop':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <html>
            <head><title>Encuesta sobre el cielo</title></head>
            <body>
            <h2>El servidor ha sido detenido</h2>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
            # Detener el servidor
            self.server.shutdown()
   
    def do_POST(self):
        # Código para procesar la respuesta del usuario
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        respuesta = int(post_data.split('=')[1])
        respuestas.append(respuesta)
        # Código para servir una página de confirmación
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

respuestas = []

if __name__ == '__main__':
    server_address = ('', 3000)
    httpd = http.server.HTTPServer(server_address, SurveyHandler)
    httpd.serve_forever()

def generar_grafica():
    # Código para generar la gráfica de barras con los resultados de la encuesta
    valores = [respuestas.count(i) for i in range(1, 11)]
    etiquetas = [str(i) for i in range(1, 11)]
    plt.bar(etiquetas, valores)
    plt.xlabel('Respuesta')
    plt.ylabel('Número de votos')
    plt.title('Resultados de la encuesta sobre el cielo')
    plt.savefig('grafica.png')  # Guardar la gráfica en formato PNG
    plt.show()
""" 
def generar_grafica():
    # Obtener los resultados de la encuesta
    resultados = respuestas()

    # Generar la gráfica
    x = range(1, 11)
    y = [resultados[str(i)] for i in x]
    plt.bar(x, y)
    plt.xlabel('Puntuación')
    plt.ylabel('Número de respuestas')
    plt.title('Encuesta sobre el cielo')
    plt.savefig('grafica.png')  # Guardar la gráfica en formato PNG """


""" if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, SurveyHandler)
    httpd.serve_forever()
    generar_grafica()
 """

if __name__ == '__main__':
    try:
        server_address = ('', 3000)
        httpd = http.server.HTTPServer(server_address, SurveyHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('Servidor detenido')
    finally:
        generar_grafica()
