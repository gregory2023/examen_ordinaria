import unittest
from jugador import Player
from game import Game

class Test(unittest.TestCase):
    def test1(self):
        player = Player(1, 'a')
        self.assertEqual(player.getEnergy(), (MAX_ENERGY + MIN_ENERGY) // 2)

    def test2(self):
        player = Player(1, 'a')
        player.boost(-100)
        self.assertTrue(player.getEnergy() == MIN_ENERGY)

    def test3(self):
        player = Player(1, 'a')
        player.boost(200)
        self.assertTrue(player.getEnergy() == MAX_ENERGY)

    def test4(self):
        p1 = Player(1, 'a')
        p2 = Player(2, 'b')
        game = Game(p1, p2, 1)
        game.play()
        if p1.getEnergy() > p2.getEnergy():
            self.assertEqual(game.winner(), p1)
        elif p2.getEnergy() > p1.getEnergy():
            self.assertEqual(game.winner(), p2)
        else:
            self.assertIsNone(game.winner())

if __name__ == "__main__":
    unittest.main()
