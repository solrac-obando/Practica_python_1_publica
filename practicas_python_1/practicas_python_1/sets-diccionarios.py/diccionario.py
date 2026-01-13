"""
Los diccionarios son similares a las lista pero en lugar de tener un índice numérico tiene
un índice alfanumérico, también se distinge porque funciona como un objeto JSON en otras palabras
guarda datos en un formato (clave:valor) o llave, el diccionario utiliza {} para crearlos

"""
person= {
    "nombre": "Carlos",
    "apellido": "Perez",
    "edad": "20",
}
print(person)
print(person["edad"])# usando la clave al imprimir se puede extraer el valor

print("\n############### Ejercicio 2 #############\n")

#listas con diccionarios

contactos = [

    {
        "Nombre":"Carlos Obando",
        "web":"carlos@example.com",
        "edad":30,
    },
     {
        "Nombre":"Luis Robles",
        "web":"luis@example.com",
        "edad":20,
    },
     {
        "Nombre":"Maria Aure",
        "web":"maria@example.com",
        "edad":55,
    },
     {
        "Nombre":"Laura Perez",
        "web":"laura@example.com",
        "edad":17,
    }
]
print(contactos)
contactos[0]["Nombre"] = "arlos Obando"
print(contactos[0]["Nombre"])

for contacto in contactos:
    print(f"El Nombre del contacto es: {contacto["Nombre"]} y su web es: {contacto["web"]}")
print("\n")