import util.conexion as cnx
import mysql.connector
from CTkMessagebox import CTkMessagebox as Message

class Usuario():
    def getByCorreo(correo):
        conn = cnx.conectar()
        consulta = "SELECT * FROM Usuarios WHERE Correo=%s"
        user = None
        try:
            cursor = conn.cursor()
            cursor.execute(consulta,(correo,))
            user = cursor.fetchone()
        except mysql.connector.Error as err:
            Message(title="Error de base de datos", message=err, icon="cancel")
        conn.close()
        return user
        
