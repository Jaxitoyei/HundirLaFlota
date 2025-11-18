class Barco:

    def __str__(self):
        self.nombre=""
        self.size = 5
        self.icono = "[]"
        self.cordX=0;
        self.cordY=0;



    def getCordX(self):
        return self.cordX

    def setCordX(self,cordx):
        self.cordX=cordx

    def getCordY(self):
        return self.cordY

    def setCordY(self, cordy):
        self.cordY = cordy

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size=size

    def getNombre(self, nombre):
        return self.nombre

    def getIcon(self):
        return self.icono