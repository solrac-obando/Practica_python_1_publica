"""
Esta es la Introduccion de la programacion orientada a objetos (POO)
es un paradicma de como se puede observar el mundo y este concepto aplicado a la programacion. 
es como a travez de codigo se puedes espresa todas las caracteristicas de un objeto 
en el mundo real y sus acciones por medio del codigo, y como aplicar estos objetos en diferentes situaciones.
los fundamentos de la POO se las (class) o clases y los (methons) o metodos y funciones.
una clases es un molde para crear objetos que comparten caracteristicas similares esta tiene atributos y/o propiedades

"""

class carro:
    # Atributos o propiedades (variables)
    # Caracteristicas del Carro
    color ="Rojo"
    marca = "Toyota"
    modelo = "Corolla"
    velocidad = 200
    caballaje = 300
    plazas = 5

    # Metodos = acciones que hace el objeto (funciones)
    def acelerar(self):
        self.velocidad += 1
        
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    # finalizacion de definicion de la clase del ejercicio 1 velocidad

    def setcolor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setmodelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo

    

    # Crear objeto / Instaciar la clase
mi_carro = carro()
mi_carro.setcolor("Azul")
print(mi_carro.marca, mi_carro.getModelo() ,mi_carro.getColor())
print(f"La velocidad actual es {mi_carro.velocidad}")

mi_carro.acelerar()
mi_carro.acelerar()
mi_carro.acelerar()
mi_carro.frenar()
print(f"La velocidad nueva es {mi_carro.getVelocidad()}")