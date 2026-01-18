"""
La Herencia en la programacion orientada a objetos es la pocibilidad de heredar propiedades
y/o atributos de una clase a otra esto ocurre principalmente si son clases relacionadas entre si
y que tendan un orden geragico de padre - hijo, es decir que sea de un orden superior la clase padre
para que la clase hijo pueda heredar los atributos de su clase padre.

La Herencia se puede hacer de dos formas de acuerdo a si es una herencia simple o compuesta.
Una herencia simple ocurre cuando la clase hijo solo hereda atributos y metodos de su clase padre. 
Una Herencia compuesta es cuando la clase hijo hereda atributos y metodos de su clase padre y también de otra clase.
"""


class Persona():
    
    #Atributos de referencia: Nombre, Apellido, Edad, Altura
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getEdad(self):
        return self.edad
    def getAltura(self):
        return self.altura 
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setEdad(self, edad):
        self.edad = edad
    def setAltura(self, altura):
        self.altura = altura
    def getInfo(self, info_persona):
        info_persona = "----- Informacion de la persona -----"
        info_persona += "El Nombre es: " + self.getNombre()
        info_persona += "El Apellido es: " + self.getApellido()
        info_persona += "La Edad es: " + self.getEdad()
        info_persona += "Su Altura es: " + self.getAltura()

    def Hablar(self):
        return "Hola Estoy Hablando"
    def Caminar(self):
        return "Hola Estoy Caminado al trabajo"
    def Dormir(self):
        return "Hola Voy a tomar una siesta"
    
class Informatico(Persona):
    # #Atributos de referencia: Lenguajes, Experiencias
    def __init__(self):
        self.lenguajes = "HTML, CSS, PYTHON, N8N, JAVASCRIPT(BASICO)"
        self.experiencia = str(3) + " Year en la industria"
    def getLenguajes(self):
        return self.lenguajes
    def getExperiencia(self):
        return self.experiencia
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    def programar(self):
        return "Estoy Programando 2 Proyectos una personal, y otro laborar de una Agropecuaria"
    def repararPc(self):
        return "Tu computadora ya esta reparada fue un gusto atenderle," \
        " y estamos a la orden para cualquier otras cosa"

class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__()
        self.auditorRedes = 'Experto'
        self.experienciaRedes = 10

    def auditoria(self):
        return "Estoy Auditando las redes del Bancon, llamarme mas tarde: "

    