import mysql.connector

try:
    # Conexión
    database = mysql.connector.connect(
        host="localhost",
        user="estudiante",
        passwd="1234",
        database="master_python"
    )

    # print(database)
    cursor = database.cursor(buffered=True)

    cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
    # cursor.execute("SHOW DATABASES")

    # for bd in cursor:
    #     print(bd)

    print("\n")
    # Crear una tabla
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS vehiculos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                     color VARCHAR(45) NOT NULL,
                     marca VARCHAR(45) NOT NULL,
                    modelo VARCHAR(45) NOT NULL,
                    velocidad INT(10) NOT NULL,
                    precio DECIMAL(10,2) NOT NULL)
                    """)

    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)

    # Insertar datos en la tabla

    # cursor.execute("INSERT INTO vehiculos VALUES (null,'rojo','ford','mustang',300, 18500)")

    carros = [
        ('negro', 'seat', 'ibiza', 220, 8500),
        ('azul', 'Toyota', 'corolla', 250, 9500),
        ('gris', 'Renault', 'Logan', 240, 8500),
    ]
    # cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s, %s, %s)", carros)

    database.commit()

    # Extraer datos o consultar datos

    cursor.execute("SELECT * FROM vehiculos")  # mostrar todos los datos
    # cursor.execute("SELECT * FROM vehiculos WHERE precio >= 9000 AND velocidad <= 280")  # mostrar con condiciones a través de un WHERE

    resultado = cursor.fetchall()

    print("----------- Mostrar datos de la tabla -------------")
    for contador in resultado:
        print(contador)

    # resul1 = cursor.fetchone()
    # print(resul1[2])

    # Borrar registros en la tabla

    cursor.execute("DELETE FROM vehiculos WHERE marca = 'Toyota'")
    database.commit()
    print(cursor.rowcount, "registros borrados")

    # Actualizar datos
    cursor.execute("UPDATE vehiculos SET modelo= 'clio' WHERE marca= 'Renault'")
    database.commit()

    # Mostrar datos actualizados
    cursor.execute("SELECT * FROM vehiculos")
    resultado_actualizado = cursor.fetchall()
    print("----------- Datos actualizados -------------")
    for fila in resultado_actualizado:
        print(fila)

except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'database' in locals():
        database.close()
    print("Conexión cerrada.")