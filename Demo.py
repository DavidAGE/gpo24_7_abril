class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

NumLado = Cuadrado(50)
print ("Elarea del cuadrado es:", NumLado.area())

#############################################
lado = int(input("Ingresa el lado?"))
mi_ejemplo = Cuadrado(lado)
r = mi_ejemplo.area()
print(f'El area es: {r}')