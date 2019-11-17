import unittest

from bowling import score_game, total_score, spare_score

gutter_game = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
simple_game = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
strike_game = [[10],[10],[10],[10],[10],[10],[10],[10],[10],[10],[10],[10]]
spare_game = [[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5]]
complex_game = [[6,1],[9,0],[8,2],[5,5],[8,0],[6,2],[9,1],[7,2],[8,2],[9,1],[7]]
spare_test_data = [[8,2],[6,2]]

class GutterGame(unittest.TestCase):

    def test_final_score(self):
        print("####Testing Gutter Game####")
        final = total_score(gutter_game)
        self.assertEqual(final, 0, "should be zero")

class SimpleGame(unittest.TestCase):

    def test_simple_game(self):
        print("####Testing Simple Game####")
        final = total_score(simple_game)
        self.assertEqual(final, 20, "Shold be 20")

class Spare(unittest.TestCase):

    def test_spare(self):
        print("####Testing Spare Function####")
        total = spare_score(0, spare_test_data)
        self.assertEqual(total, 16, "Should be 16")
    
    def test_spare_game(self):
        print("####Testing Spare Game####")
        final = total_score(spare_game)
        self.assertEqual(final, 150, "Should be 150")

class StrikeGame(unittest.TestCase):

    def test_strike_game(self):
        print("####Testing Strike Game####")
        final = total_score(strike_game)
        self.assertEqual(final, 300, "Should be 300")

class ComplexGame(unittest.TestCase):

    def test_complex_game(self):
        print("####Testing Complex Game####")
        final = total_score(complex_game)
        self.assertEqual(final, 127, "Should be 127")

if __name__ == '__main__':
    unittest.main()

