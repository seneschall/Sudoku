from pprint import pp
from random import randint
from helpers import gen_coord

type GameGrid = list[list[int]]


def is_in_row_of(x: int, y: int, val: int) -> bool:
    pass


def is_in_column_of(x: int, y: int, val: int) -> bool:
    pass


def is_in_region_of(x: int, y: int, val: int) -> bool:
    pass


def possible_solution(x: int, y: int, val: int) -> bool:
    """
    Would it violate the rules to place val in the cell at (x,y)?
    """
    if (
        is_in_row_of(x, y, val)
        or is_in_column_of(x, y, val)
        or is_in_region_of(x, y, val)
    ):
        return False

    return True


def simple_solver(grid: GameGrid) -> None:
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for v in range(1, 10):
                    if possible_solution(x, y, v):
                        grid[y][x] = v
                    simple_solver(grid)
                    return
    return


def remove_vals(grid: GameGrid, count: int) -> None:
    """
    Removes a given number of values from the given grid by setting them to 0.
    """
    while count != 0:
        x, y = gen_coord()
        if grid[y][x] == 0:  # if value has already been removed, try again
            continue
        val: int = randint(1, 9)
        grid[y][x] = val
        count -= 1


def make_game(clue_count: int) -> GameGrid:
    """
    Makes a valid sudoku grid with the given number of clues.
    """
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    game: GameGrid = simple_solver(grid)
    remove_count: int = (9 * 9) - clue_count
    remove_vals(game, remove_count)
    return game


if __name__ == "__main__":
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    game = simple_solver(grid)
    pp(game)
