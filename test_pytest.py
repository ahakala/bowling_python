import pytest

from bowling import score_game, total_score, spare_score

gutter_game = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
simple_game = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
strike_game = [[10],[10],[10],[10],[10],[10],[10],[10],[10],[10],[10],[10]]
spare_game = [[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5]]
complex_game = [[6,1],[9,0],[8,2],[5,5],[8,0],[6,2],[9,1],[7,2],[8,2],[9,1],[7]]
spare_test_data = [[8,2],[6,2]]


def test_final_score():
    print("####Testing Gutter Game####")
    final = total_score(gutter_game)
    assert final == 0 


def test_simple_game():
    print("####Testing Simple Game####")
    final = total_score(simple_game)
    assert final == 20 


def test_spare():
    print("####Testing Spare Function####")
    total = spare_score(0, spare_test_data)
    assert total == 16

def test_spare_game():
    print("####Testing Spare Game####")
    final = total_score(spare_game)
    assert final == 150


def test_strike_game():
    print("####Testing Strike Game####")
    final = total_score(strike_game)
    assert final == 300


def test_complex_game():
    print("####Testing Complex Game####")
    final = total_score(complex_game)
    assert final == 127
if __name__ == '__main__':
    pytest.main()

