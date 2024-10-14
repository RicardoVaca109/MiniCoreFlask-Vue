from flask import Blueprint, jsonify, request
from models.vehiculos import VehiculosModel

vehiculos_bp = Blueprint('vehiculos_bp', __name__)

@vehiculos_bp.route('/vehiculos', methods=['GET'])
def obtener_vehiculos():
    try:
        vehiculos = VehiculosModel.obtener_vehiculos()
        return jsonify(vehiculos), 200
    except Exception as e:
        return jsonify({'mensaje': 'Error al obtener los vehículos', 'error': str(e)}), 500

@vehiculos_bp.route('/vehiculos', methods=['POST'])
def agregar_vehiculo():
    try:
        datos = request.json
        id_propietario = datos.get('id_propietario')
        marca = datos.get('marca')
        modelo = datos.get('modelo')
        placa = datos.get('placa')
        color = datos.get('color')
        tipo_vehiculo = datos.get('tipo_vehiculo')
        
        # Llamar al modelo para agregar el vehículo
        VehiculosModel.agregar_vehiculo(id_propietario, marca, modelo, placa, color, tipo_vehiculo)
        return jsonify({'mensaje': 'Vehículo agregado exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': 'Error al agregar el vehículo', 'error': str(e)}), 500

@vehiculos_bp.route('/vehiculos/<int:id>', methods=['PUT'])
def editar_vehiculo(id):
    data = request.json
    VehiculosModel.editar_vehiculo(id, data['marca'], data['modelo'], data['placa'], data['color'], data['tipo_vehiculo'])
    return jsonify({'message': 'Vehículo actualizado exitosamente'})

@vehiculos_bp.route('/vehiculos/<int:id>', methods=['DELETE'])
def eliminar_vehiculo(id):
    VehiculosModel.eliminar_vehiculo(id)
    return jsonify({'message': 'Vehículo eliminado exitosamente'})
    