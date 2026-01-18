"""
Este es el ejercicio de manejo de errores:
para manejar errores en Python hay que utilizar los siguientes comandos
try: para el código que está que puede generar un posible error y
except: para el código que se ejecutará cuando el error del try sea confirmado
en otras palabras el except es para control de daños en caso de que ocurra un error se ejecutará
las instrucciones o el código de manejo de errores, se puede entender que es como un condicional
especializado en el manejo de errores

es para manejar código susceptible a fallos
"""

nombre = input("ingrese su nombre: ")
#print(nombre)
try:
    if len(nombre) > 1:
        nombre_usuario = f"El nombre es {nombre}"
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, por favor coloca un nombre válido.")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin del programa")


Lista_numeros=[
    13,25,31,49,5,16,37,68,
]

#hacer una función que recorra la lista y devuelva un string
def mostraLista(lista):
    resultado=""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado


print("########### Ejercicio de manejo de errores 2 #############\n")

print(mostraLista(Lista_numeros))

print("############### Ordena y mostrar ##############\n")

Lista_numeros.sort()
print(mostraLista(Lista_numeros))

print("############### mostrar la longitud ##############\n")
print(len(Lista_numeros))

print("############### busqueda ##############\n")
try:
    busqueda= int(input("Introduce un número para verificar en la lista: "))
    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda= int(input("Introduce un número para verificar en la lista"))
    else:
        print(f"Has introducido el número: {busqueda}", "\n")

#try:
    search = Lista_numeros.index(busqueda)
    print(f"##### El número buscado sí existe en la lista es: {busqueda}", "############\n")
    print(f" El número ingresado en la búsqueda existe en la lista, con el índice: {search}")

except IndexError:
    print("Ha ocurrido un error el número que introdujo no está en la lista \n " \
    "pruebe con otro número")
except ValueError:
   print("Ha ocurrido un error recuerda que el dato para buscar debe ser un número")
except Exception as e:
    print(f"Ha ocurido un error de tipo {type(e).__name__}")
    print(type(e))
finally:
    print("Fin del programa")

# Excepciones personalizadas o Lanzar excepcion
try:
    nombre_usuario = input("Hola por favor dime tu Nombre Completo: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 100:
        raise ValueError(f"La edad Introducida es Falsa {edad}, la edad no puede ser menor de 5 o mayor a 100")
    elif len(nombre_usuario) <= 1:
        raise ValueError("El nombre introducido no esta completo, por favor introduce tu nombre completo")
    else:
        print(f"Bienvenido al sistema, {nombre_usuario}")
except ValueError:
    print("Ha ocurrido un error recuerda Introducir los datos correctos y completos")
except Exception as i:
    print(f"Ha ocurido un error de tipo {type(i).__name__}")
    print(type(i))
