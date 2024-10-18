from src.grid import Grid

def test_a_cell_stays_alive_if_it_has_two_neighbors():
    grid = Grid(3, 3, {
        (0, 0), (1, 0), (2, 0),
    })
    assert (1, 0) in grid.next_generation().living_cells

def test_a_cell_stays_alive_if_it_has_three_neighbors():
    grid = Grid(3, 3, {
                (1, 0),
        (0, 1), (1, 1), (2, 1),
    })
    assert (1, 1) in grid.next_generation().living_cells

def test_a_cell_becomes_alive_if_it_has_three_neighbors():
    grid = Grid(3, 3, {
                (1, 0),
        (0, 1),
                (1, 2),
    })
    assert (1, 1) in grid.next_generation().living_cells

def test_a_cell_dies_from_overpopulation_if_it_has_more_than_three_neighbors():
    grid = Grid(3, 3, {
                (1, 0),
        (0, 1), (1, 1), (2, 1),
                (1, 2),
    })
    assert (1, 1) not in grid.next_generation().living_cells

def test_a_cell_dies_from_underpopulation_if_it_has_less_than_two_neighbors():
    grid = Grid(3, 3, {
        (0, 0), (1, 0),
    })
    assert (1, 0) not in grid.next_generation().living_cells
