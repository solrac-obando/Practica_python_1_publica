import mysql.connector

class Conectar:
    def __init__(self):
        self.database = mysql.connector.connect(
            host='localhost',
            user='estudiante',
            passwd='1234',
            database='notas_tech',
            port=3306
        )
        self.cursor = self.database.cursor(buffered=True)

    def get_connection(self):
        return [self.database, self.cursor]
   
