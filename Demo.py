class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

NumLado = Cuadrado(50)
print ("Elarea del cuadrado es:", NumLado.area())

