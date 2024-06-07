import math


class EquiFigura:
    def __init__(self, longitudLados):
        self.__longitudLados = longitudLados

    def getLongitudLados(self):
        return self.__longitudLados

    def setLongitudLados(self, longitudLados):
        self.__longitudLados = longitudLados

    def toString(self):
        return f'Longitud de Lados: {self.__longitudLados}'


class TrianguloEquilatero(EquiFigura):
    def getPerimetro(self):
        return 3 * self.getLongitudLados()

    def getArea(self):
        lado = self.getLongitudLados()
        return (math.sqrt(3) / 4) * (lado ** 2)

class Cuadrado(EquiFigura):
    def getPerimetro(self):
        return 4 * self.getLongitudLados()

    def getArea(self):
        lado = self.getLongitudLados()
        return lado ** 2


def getPerimetroFigura(figura):
    return figura.getPerimetro()


def getAreaFigura(figura):
    return figura.getArea()


te1 = TrianguloEquilatero(3)
cu1 = Cuadrado(4)


print(f'Triángulo Equilátero (lado 3) - Perímetro: {getPerimetroFigura(te1)}, Área: {getAreaFigura(te1)}')


print(f'Cuadrado (lado 4) - Perímetro: {getPerimetroFigura(cu1)}, Área: {getAreaFigura(cu1)}')
