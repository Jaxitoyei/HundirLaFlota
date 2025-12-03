class Barco:

    def __init__(self,nombre,tamaño):

        self.nombre=nombre
        self.size = tamaño
        self.icono = "Ç"
        self.cordX=0
        self.cordY=0
        self.orientacion="o"
        self.isSinking=False



    def getCordX(self):
        return self.cordX

    def setCordX(self, cordx):
        self.cordX = cordx

    def getCordY(self):
        return self.cordY

    def setCordY(self,cordy):
        self.cordY=cordy

    def getSize(self):
        return self.size

    def getName(self):
        return self.nombre

    def setOrientation(self,orientation):
        self.orientacion=orientation

    def getOrientation(self):
        return self.orientacion

    def __str__(self):
        return f"Nombre del barco: {self.nombre}, tamaño del barco: {self.size}"