class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada):
        super().__init__(color="azul", ruedas=4, puertas=4)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Mi vehiculo es de tipo Coche color: {}, Tiene {} ruedas, y es de {} puertas. Corre a una velocidad de {} km/h, y es de {} cc".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)


mi_coche = Coche(120, 1600)
print(mi_coche)