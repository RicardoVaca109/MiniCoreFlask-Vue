# Importar librerias a usarse
from flask import Flask, jsonify
from flask_cors import CORS
from controllers.greetings_controller import greetings_bp
from controllers.shark_controller import shark_bp
from controllers.vehiculos_controllers import vehiculos_bp
from controllers.propietarios_controller import propietarios_bp
import os

# Instanciamos una aplicacion de tipo FLask
app = Flask(__name__)

# Actualizar la aplicacion constantemente
app.config.from_object(__name__)

# Habilitar CORS (Cross Origin Resource Sharing)
CORS(app, resources={r"/*":{'origins':"*"}}) 

app.register_blueprint(greetings_bp)
app.register_blueprint(shark_bp)
app.register_blueprint(vehiculos_bp)
app.register_blueprint(propietarios_bp)

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True) 
    
# # Ruta para un Hello World
# @app.route('/', methods = ['GET'])
# def greetings():
#     return('Hello World!')

# app.register_blueprint(greetings_bp)
# app.register_blueprint(shark_bp)

# # Ruta para shark y usar Axios para conectar al frontend
# @app.route('/shark', methods = ['GET'])
# def shark():
#     return('Esto es shark')    