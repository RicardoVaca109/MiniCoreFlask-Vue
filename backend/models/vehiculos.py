from database import conexion_database

#modelo vehiculos

class VehiculosModel:
    
    @classmethod
    def obtener_vehiculos(cls):
        cursor = conexion_database.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.id, v.marca, v.modelo, v.placa, v.color, v.tipo_vehiculo, p.nombre AS propietario, p.telefono, p.correo 
            FROM vehiculos v
            JOIN propietarios p ON v.id_propietario = p.id
        """)
        vehiculos = cursor.fetchall()
        cursor.close()
        return vehiculos
    
    @classmethod
    def agregar_vehiculo(cls, id_propietario, marca, modelo, placa, color, tipo_vehiculo):
        cursor = conexion_database.cursor()
        cursor.execute(
            "INSERT INTO vehiculos (id_propietario, marca, modelo, placa, color, tipo_vehiculo) VALUES (%s, %s, %s, %s, %s, %s)",
            (id_propietario, marca, modelo, placa, color, tipo_vehiculo)
        )
        conexion_database.commit()
        cursor.close()
        
    @classmethod
    def editar_vehiculo(cls, id, marca, modelo, placa, color, tipo_vehiculo):
        cursor = conexion_database.cursor()
        cursor.execute(
            """
            UPDATE vehiculos 
            SET marca = %s, modelo = %s, placa = %s, color = %s, tipo_vehiculo = %s 
            WHERE id = %s
            """,
            (marca, modelo, placa, color, tipo_vehiculo, id)
        )
        conexion_database.commit()
        cursor.close()

    @classmethod
    def eliminar_vehiculo(cls, id):
        cursor = conexion_database.cursor()
        cursor.execute("DELETE FROM vehiculos WHERE id = %s", (id,))
        conexion_database.commit()
        cursor.close()