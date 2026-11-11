import mysql.connector
from CTkMessagebox import CTkMessagebox as Message
from dotenv import load_dotenv
import util.generic as utl
import os

load_dotenv()

def conectar():
     try:
        conexion = mysql.connector.connect(user=os.getenv('USER'), password=os.getenv('PASS'), host=os.getenv('HOST'), database=os.getenv('DB'), port=os.getenv('PORT'))
        return conexion
     except mysql.connector.Error as err:
        Message(title='Error de base de datos', message=err, icon='cancel')

def createAdmin():
    conn = mysql.connector.connect(user=os.getenv('USER'), password=os.getenv('PASS'), host=os.getenv('HOST'), database=os.getenv('DB'), port=os.getenv('PORT'))
    consulta = 'SELECT ID_Usuario FROM Usuarios WHERE Correo=%s'
    try:
        cursor = conn.cursor()
        cursor.execute(consulta,('admin@admin.com',))
        user = cursor.fetchone()
        if not user:
            entry = 'INSERT INTO Usuarios (Correo, Contraseña, Nombre, Rol) VALUES (%s,%s,%s,%s)'
            password = utl.hash(os.getenv('PASS2'))
            datos = (os.getenv('EMAIL'), password , 'Admin', 'Administrador')
            cursor.execute(entry,datos)
            conn.commit()
    except mysql.connector.Error as err:
        Message(title="Error de base de datos", message=err, icon="cancel")
    conn.close()