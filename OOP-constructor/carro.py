"""
Docstring for OOP-constructor.main
se copio la clase carro de la carpeta POO para trabajar sobre este ejemplo

"""

class carro:
    color ="Rojo"
    marca = "Toyota"
    modelo = "Corolla"
    velocidad = 200
    caballaje = 300
    plazas = 5

    soy_publico = "Hola soy una propiedad de ejemplo que es publica "
    __soy_privado = "Hola Soy una propiedad de ejemplo Privada"

# definir un constructor se realiza despues de crear los atributos con una def __init__ 
#ese constructor debe ser la primera funcion o metodo de la clase.
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        #self.__soy_privado = "Hola Soy una propiedad de ejemplo Privada"

    # finalizacion de definicion de la clase del ejercicio 1 velocidad


    def getPrivado(self):
        return self.__soy_privado
    
    def setcolor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setmarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    def setmodelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo
    def setvelocidad(self, velocidad):
        self.velocidad = velocidad
    def acelerar(self):
        self.velocidad += 1   
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad
    def getinfo(self):
        info = "----- Informacion del carro -----"
        info += "\n Color: " + self.getColor()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Marca: " + self.getMarca()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info

  