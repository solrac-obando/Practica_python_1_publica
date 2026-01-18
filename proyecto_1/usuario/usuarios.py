import usuario.conexion as conexion
import datetime
import hashlib

connet = conexion.Conectar()
database, cursor = connet.get_connection()
class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    def registrar(self):
        # cifrado del password
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) # el valor necesita estar en bits
        
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            resultado = [cursor.rowcount, self]
        except:
            resultado = [0, self]
        return resultado

    def identificar(self):
        # consulta para comprobar si exista un usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        #datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result

        