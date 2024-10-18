from collections import defaultdict
from collections.abc import ItemsView
from typing import Set, List, Tuple, DefaultDict

class Grid:
    NEIGHBOR_OFFSETS = [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0),
        (-1,  1), (0,  1), (1,  1),
    ]

    def next_generation(self) -> 'Grid':
        return Grid(self.width, self.height, {
            cell for cell, neighbors in self.__neighbor_counts_for_all_cells()
            if 3 == neighbors or (2 == neighbors and self.__is_living(cell))
        })

    def __init__(self, width: int, height: int, cells: Set[Tuple[int, int]]) -> None:
        self.width = width
        self.height = height
        self.living_cells = cells

    def __is_living(self, cell: Tuple[int, int]) -> bool:
        return cell in self.living_cells

    def __neighbor_counts_for_all_cells(self) -> ItemsView[Tuple[int, int], int]:
        counts = defaultdict(int)
        for cell in self.living_cells:
            for neighbor in self.__neigbors_of(cell):
                counts[neighbor] += 1
        return counts.items()

    def __neigbors_of(self, cell: Tuple[int, int]) -> List[Tuple[int, int]]:
        x, y = cell
        return [
            neighbor for x_offset, y_offset in Grid.NEIGHBOR_OFFSETS
            if self.__is_within_boundaries_of_grid(neighbor := (x + x_offset, y + y_offset))
        ]

    def __is_within_boundaries_of_grid(self, cell: Tuple[int, int]) -> bool:
        x, y = cell
        return 0 <= x < self.width and 0 <= y < self.height
