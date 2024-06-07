from jugador import Player
from game import Game

# Creación de jugadores
p1 = Player(1, 'a')
p2 = Player(2, 'b')

# Creación del juego
g1 = Game(p1, p2, 3)

# Mostrar los datos de los jugadores
print("Datos de los jugadores:")
print(p1.toString())
print(p2.toString())
print()

# Jugar las rondas
g1.play()

# Determinar el ganador
winner = g1.winner()

# Mostrar el ganador
if winner is None:
    print("El juego ha terminado en empate.")
else:
    print(f"El ganador es: {winner.toString()}")
