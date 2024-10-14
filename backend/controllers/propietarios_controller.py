from flask import Blueprint, jsonify, request
from models.propietarios import PropietariosModel  # Asegúrate de que el path sea correcto

# Crear un Blueprint para el controlador de propietarios
propietarios_bp = Blueprint('propietarios_bp', __name__)

# Ruta para obtener todos los propietarios
@propietarios_bp.route('/propietarios', methods=['GET'])
def obtener_propietarios():
    try:
        propietarios = PropietariosModel.obtener_propietarios()
        return jsonify(propietarios), 200
    except Exception as e:
        return jsonify({'mensaje': 'Error al obtener los propietarios', 'error': str(e)}), 500

# Ruta para agregar un nuevo propietario
@propietarios_bp.route('/propietarios', methods=['POST'])
def agregar_propietario():
    try:
        datos = request.json
        nombre = datos.get('nombre')
        telefono = datos.get('telefono')
        correo = datos.get('correo')
        
        # Llamar al modelo para agregar el propietario
        PropietariosModel.agregar_propietario(nombre, telefono, correo)
        return jsonify({'mensaje': 'Propietario agregado exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': 'Error al agregar el propietario', 'error': str(e)}), 500