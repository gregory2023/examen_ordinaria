
MAX_ENERGY = 100
MIN_ENERGY = 0
MIN_=0


class Player:

    def __init__(self, idPlayer, nickName):
        self.__idPlayer = idPlayer
        self.__nickName = nickName
        self.__energy = (MAX_ENERGY + MIN_ENERGY) // 2


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


    def toString(self):
        return f'[{self.__idPlayer}, {self.__nickName}, {self.__energy}]'


    def boost(self, charge):
        if not isinstance(charge, int):
            charge = 0

        new_energy = self.__energy + charge


        if new_energy > MAX_ENERGY:
            new_energy = MAX_ENERGY
        elif new_energy < MIN_ENERGY:
            new_energy = MIN_ENERGY

        self.__setEnergy(new_energy)

        return charge, self.__energy



if __name__ == "__main__":
    player = Player(1, "Jugador1")
    print(player.toString())

    print(player.boost(30))

    print(player.boost(-90))

    print(player.boost(200))

    print(player.boost('a'))

    print(player.toString())
