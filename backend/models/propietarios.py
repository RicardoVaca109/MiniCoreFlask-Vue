from database import conexion_database

#Modelo propietarios
class PropietariosModel:
    @classmethod
    def obtener_propietarios(cls):
        cursor = conexion_database.cursor(dictionary=True)
        cursor.execute("SELECT * FROM propietarios")
        propietarios = cursor.fetchall()
        cursor.close()
        return propietarios
    
    @classmethod
    def agregar_propietario(cls, nombre, telefono, correo):
      cursor = conexion_database.cursor()
      cursor.execute("INSERT INTO propietarios (nombre, telefono, correo) VALUES (%s, %s, %s)",
                     (nombre, telefono, correo))
      conexion_database.commit()
      cursor.close()
    
    
      