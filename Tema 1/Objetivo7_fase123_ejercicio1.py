#José Carlos Mora 2ºDAM

class Vehiculo:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, v):
        self.velocidad += v

    def desacelerar(self, v):
        self.velocidad -= v
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_velocidad(self):
        print(f"Tu velocidad actual es: {self.velocidad} km/h")

class Coche(Vehiculo):
    def __init__(self, marca, velocidad=0, bocina="¡tuuut!"):
        super().__init__(marca, velocidad)
        self.bocina = bocina

    def tocar_claxon(self):
        print(self.bocina)


coche_1 = Coche("Peugeot 208", 10.5)
print(f"La velocidad inicial del coche es: {coche_1.velocidad}")
coche_1.acelerar(50)
coche_1.desacelerar(15)
coche_1.mostrar_velocidad()
coche_1.tocar_claxon()
