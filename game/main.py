#https://github.com/gregory2023/examen_ordinaria/tree/master

from jugador import Player
from game import Game


p1 = Player(1, 'a')
p2 = Player(2, 'b')


g1 = Game(p1, p2, 3)


print("Datos de los jugadores:")
print(p1.toString())
print(p2.toString())
print()


g1.play()


winner = g1.winner()


if winner is None:
    print("El juego ha terminado en empate.")
else:
    print(f"El ganador es: {winner.toString()}")
