class Barco:

    def __init__(self,nombre,tamaño):

        self.__nombre=nombre
        self.__size = tamaño
        self.__cordX=0;
        self.__cordY=0;
        self.__orientacion="o"
        self.__isSinking=False;
        self.__cords=[]

    @property
    def getCordX(self):
        return self.__cordX

    def setCordX(self, cordx):
        self.__cordX = cordx

    @property
    def getCordY(self):
        return self.__cordY

    def setCordY(self,cordy):
        self.__cordY=cordy

    @property
    def getSize(self):
        return self.__size

    @property
    def getName(self):
        return self.__nombre

    def setOrientation(self,orientation):
        self.__orientacion=orientation

    @property
    def getOrientation(self):
        return self.__orientacion

    @property
    def hundido(self):
        self.isSinking=True

    def agregaCords(self,cord):
        if len(self.__cords)<self.getSize:
            self.__cords.append(cord)

    @property
    def getCords(self):
        return self.__cords

    def __str__(self):
        return f"Nombre del barco: {self.__nombre}, tamaño del barco: {self.__size}"