
MAX_ENERGY = 100
MIN_ENERGY = 0


class Player:
    # Método constructor
    def __init__(self, idPlayer, nickName):
        self.__idPlayer = idPlayer
        self.__nickName = nickName
        self.__energy = (MAX_ENERGY + MIN_ENERGY) // 2

    # Métodos get/set
    def getIdPlayer(self):
        return self.__idPlayer

    def setIdPlayer(self, idPlayer):
        self.__idPlayer = idPlayer

    def getNickName(self):
        return self.__nickName

    def setNickName(self, nickName):
        self.__nickName = nickName

    def getEnergy(self):
        return self.__energy

    def __setEnergy(self, energy):
        if MIN_ENERGY <= energy <= MAX_ENERGY:
            self.__energy = energy

    # Método toString
    def toString(self):
        return f'[{self.__idPlayer}, {self.__nickName}, {self.__energy}]'

    # Método boost
    def boost(self, charge):
        if not isinstance(charge, int):
            charge = 0

        new_energy = self.__energy + charge

        # Asegurarse de que el nuevo valor de energía esté dentro del rango permitido
        if new_energy > MAX_ENERGY:
            new_energy = MAX_ENERGY
        elif new_energy < MIN_ENERGY:
            new_energy = MIN_ENERGY

        self.__setEnergy(new_energy)

        return charge, self.__energy


# Ejemplo de uso
if __name__ == "__main__":
    player = Player(1, "Jugador1")
    print(player.toString())  # Muestra: [1, Jugador1, 50]
    print(player.boost(30))  # Muestra: (30, 80)
    print(player.boost(-90))  # Muestra: (-90, 0)
    print(player.boost(200))  # Muestra: (200, 100)
    print(player.boost('a'))  # Muestra: (0, 100)
    print(player.toString())  # Muestra: [1, Jugador1, 100]
