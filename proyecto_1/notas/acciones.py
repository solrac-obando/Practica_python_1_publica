import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"\nVamos a crear una nueva nota para {usuario[1]}!")
        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nNota guardada correctamente: {nota.titulo}")
        else:
            print("\nNo se pudo guardar la nota")

    def mostrar(self, usuario):
        print(f"\nAquí están tus notas, {usuario[1]}:")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        if len(notas) == 0:
            print("No tienes notas")
        else:
            for nota in notas:
                print("-----------------------------")
                print(f"Título: {nota[2]}")
                print(f"Descripción: {nota[3]}")
                print(f"Fecha: {nota[4]}")
                print("-----------------------------")

    def eliminar(self, usuario):
        print(f"\nVamos a eliminar una nota de {usuario[1]}!")
        titulo = input("Introduce el título de la nota a eliminar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Nota '{titulo}' eliminada correctamente")
        else:
            print("No se pudo eliminar la nota")
