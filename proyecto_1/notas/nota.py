import notas.conexion as conexion
import datetime
import hashlib

connect = conexion.Conectar()
database, cursor = connect.get_connection()

class Nota:
    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO notas VALUES(NULL, %s, %s, %s, %s)"
        nota = (self.usuario_id, self.titulo, self.descripcion, fecha)
        try:
            cursor.execute(sql, nota)
            database.commit()
            resultado = [cursor.rowcount, self]
        except:
            resultado = [0, self]
        return resultado

    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo = '{self.titulo}'"
        try:
            cursor.execute(sql)
            database.commit()
            return [cursor.rowcount, self]
        except:
            return [0, self]