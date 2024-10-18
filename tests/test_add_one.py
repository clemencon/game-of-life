from src.add_one import add_one_to
from src.game import Game

def test_answer():
    assert add_one_to(3) == 4

def test_the_grid_can_contain_living_cells():
    grid = set()
    cell = (0, 1)
    grid.add(cell)
    assert grid.pop() == cell

def test_a_game_has_a_width_and_a_height():
    game = Game(2, 4)
    assert game.width == 2
