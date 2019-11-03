import unittest

from bowling import score_game, total_score

gutter_game = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
simple_game = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
strike_game = [[10],[10],[10],[10],[10],[10],[10],[10],[10],[10],[10],[10]]
class GutterGame(unittest.TestCase):

    def test_final_score(self):
        final = total_score(gutter_game)
        self.assertEqual(final, 0, "should be zero")

class SimpleGame(unittest.TestCase):

    def test_simple_game(self):
        final = total_score(simple_game)
        self.assertEqual(final, 20, "Shold be 20")

class StrikeGame(unittest.TestCase):

    def test_strike_game(self):
        final = total_score(strike_game)
        self.assertEqual(final, 300, "Should be 300")

if __name__ == '__main__':
    unittest.main()

