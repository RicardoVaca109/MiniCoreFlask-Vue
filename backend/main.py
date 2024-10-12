# Importar librerias a usarse
from flask import Flask, jsonify
from flask_cors import CORS

# Instanciamos una aplicacion de tipo FLask
app = Flask(__name__)

# Actualizar la aplicacion constantemente
app.config.from_object(__name__)

# Habilitar CORS (Cross Origin Resource Sharing)
CORS(app, resources={r"/*":{'origins':"*"}}) 

# Ruta para un Hello World
@app.route('/', methods = ['GET'])
def greetings():
    return('Hello World!')

if __name__ == "__main__":
    app.run(debug=True)