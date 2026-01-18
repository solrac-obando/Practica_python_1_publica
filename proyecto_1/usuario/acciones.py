import usuario.usuarios as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\n Ok !! Vamos a registrarte en el sistema...")

        nombre = input("Cual es tu Nombre?: ")
        apellido = input("Cual es tu Apellido?: ")
        email = input("Cual es tu Correo?: ")
        password = input("Introduce tu Contraseña?: ")
        
        user = modelo.Usuario(nombre, apellido, email, password)
        registro = user.registrar()

        if registro[0] >= 1:
            print(f"\n Felicitaciones {registro[1].nombre}, Te has registrado correctamente con el Correo: {registro[1].email}")
        else:
            print("\n No te has registrado correctamente !!!")

    def login(self):
        print("Ok!! Entendido entonces iniciar sesión en el sistema...")
        try:
            email = input("Ingresa tu correo: ")
            password = input("Ingresa tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if login is not None:
                print(f"\n Bienvenido {login[1]}, te has identificado en el sistema en {login[5]}")
                self.proximaAccion(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login Incorrecto!! Inténtalo más tarde")

    def proximaAccion(self, usuario):
        print("""
        Acciones disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar notas (eliminar)
            - Salir de la app (salir)
""")
        nota_accion = notas.acciones.Acciones()
        acciones = input(f"Hola {usuario[1]}, ¿puedes indicar qué acción tomarás?: ")
        if acciones == "crear":
            nota_accion.crear(usuario)
            print("\n Vamos a Crear")
            self.proximaAccion(usuario)
        elif acciones == "mostrar":
            nota_accion.mostrar(usuario)
            self.proximaAccion(usuario)
        elif acciones == "eliminar":
            nota_accion.eliminar(usuario)
            self.proximaAccion(usuario)

        elif acciones == "salir":
            print(f"\n Fue un gusto {usuario[1]}, hasta luego")
            exit()