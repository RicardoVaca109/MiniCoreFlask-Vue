import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conexion_database = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),  # Revisa que tu contraseña esté correctamente establecida
    database=os.getenv('DB_NAME'),
    port=os.getenv('DB_PORT')  # Añadimos el puerto al conectar   
)