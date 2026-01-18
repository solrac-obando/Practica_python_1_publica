"""
Inicio del trabajo de base de datos con sql, en python ya hay una base de datos integrada
con el lenguajes que se está utilizando, se conoce o llama sqlite3.


"""
import sqlite3


#conexion a la base de datos
conexion = sqlite3.connect('prueba.db')


#crear un Cursor
cursor = conexion.cursor()

# crear una tablas

cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
    "id INTEGER PRIMARY KEY , "+
    "titulo VARCHAR(255), "+
    "descripcion TEXT, "+
    "precio INT (255)"+          
    ")")
#Guardar cambios en la base de datos
conexion.commit()

cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion del producto', '40')")
conexion.commit
print("-------------- Incertar datos con exito ---------------")


#lectura de datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

print(productos)
print("\n")
for producto in productos:
    print(producto)
print("\n")

# Borrar registros
cursor.execute("DELETE FROM productos")

# Insertar muchos registros a la vez
producto_1 = [
    ( 'Primer producto', 'Descripcion del producto', 40),
    ( 'Sengundo producto', 'Descripcion del producto', 450),
    ( 'tercer producto', 'Descripcion del kffioo', 800),
    ( 'Primer producto', 'Descripcion del carcomido', 60),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", producto_1)
conexion.commit()

# Cerrar conexion
conexion.close()
