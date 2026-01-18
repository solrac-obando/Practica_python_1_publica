"""
El proyecto es de python y mysql
    - Abrir un asistenete de creacion de notas por terminal
    - Login o Registro de Usuarios
    - Crear y registrar notas en una base de datos, que ademas puede (Crear notas, mostrarlas, y eliminarlas)
    - Se debe poder crear usuarios con contraseñas

"""
from usuario import acciones


print("""
Acciones disponibles:
      - registro
      - login
""")
hacerAccion = acciones.Acciones()
accion = input("Ingrese la acción que desea realizar: ")

if accion == "registro":
    hacerAccion.registro()


elif accion == "login":
    hacerAccion.login()
  