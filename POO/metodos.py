"""
Docstring for POO.metodos


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
    
    def setcolor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setmodelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo
    
# Crear mas objetos a paertir de una clases o (class) 
print("----------- Prueba de segundo objeto a partir de 1 clase-------------")
carro2 = carro()
carro3 = carro()
carro2.setmodelo("Corza")
carro2.setcolor("Verde")
print("\n Carro 2 de prueba de creacion de objeto basado en una clase \n")
print(carro2.marca, carro2.getColor(), carro2.getModelo())
# print(type(carro2))
# print(type(input))

# 