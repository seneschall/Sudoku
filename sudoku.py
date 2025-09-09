from pprint import pp
from random import randint
from helpers import gen_coord

type GameGrid = list[list[int]]
type SettableByPlayerGrid = list[list[bool]]
type PossibleValGrid = list[list[list[int]]]


class SudokuGame:
    def __init__(self, hint_count: int = 20) -> None:
        self.grid: GameGrid = make_game(hint_count)
        self.settable_by_player: SettableByPlayerGrid = (
            self.__initialise_settable_by_player()
        )
        self.possible_vals: PossibleValGrid = []
        self.__update_possible_val_grid()

    def __initialise_settable_by_player(self) -> SettableByPlayerGrid:
        result: SettableByPlayerGrid = []
        for row in self.grid:
            row_list: list[bool] = [val == 0 for val in row]
            result.append(row_list)
        return result

    def __update_possible_val_grid(self):
        new_possible_vals: PossibleValGrid = []
        for y in range(9):
            row_list: list[list[int]] = []
            for x in range(9):
                field_list: list[int] = []
                for val in range(1, 10):
                    if is_possible_solution(self.grid, x, y, val):
                        field_list.append(val)
                row_list.append(field_list)
            new_possible_vals.append(row_list)
        self.possible_vals = new_possible_vals

    def get_val_at(self, x: int, y: int) -> int:
        return self.grid[y][x]

    def regenerate(self, hint_count: int = 20) -> None:
        self.grid = make_game(hint_count)
        self.__update_possible_val_grid()

    def set_val_at(self, x: int, y: int, val: int) -> None:
        self.grid[y][x] = val
        self.__update_possible_val_grid()

    def player_settable(self, x, y) -> bool:
        return self.settable_by_player[y][x]

    def is_empty_at(self, x: int, y: int) -> bool:
        return self.grid[y][x] == 0

    def get_possible_vals_at(self, x: int, y: int) -> list[int]:
        result: list[int] = []
        for val in range(1, 10):
            if is_possible_solution(self.grid, x, y, val):
                result.append(val)
        return result


def is_in_row_of(grid: GameGrid, y: int, val: int) -> bool:
    for i in range(9):
        if grid[y][i] == val:
            return True
    return False


def is_in_column_of(grid: GameGrid, x: int, val: int) -> bool:
    for i in range(9):
        if grid[i][x] == val:
            return True
    return False


def is_in_region_of(grid: GameGrid, x: int, y: int, val: int) -> bool:
    # where in the region is x? Left, right, or centre?
    # could be refactored using `x % 3` but I'll keep it as is for legibility
    if x == 0 or x == 3 or x == 6:  # i.e. is x in left field of region?
        xs = [x, x + 1, x + 2]
    elif x == 1 or x == 4 or x == 7:  # i.e. is x in centre field of region?
        xs = [x - 1, x, x + 1]
    else:  # i.e. is x in right field of region?
        xs = [x, x - 1, x - 2]

    # where is y?
    if y == 0 or y == 3 or y == 6:  # i.e. is y in top field of region?
        ys = [y, y + 1, y + 2]
    elif y == 1 or y == 4 or y == 7:  # i.e. is x in centre field of region?
        ys = [y - 1, y, y + 1]
    else:  # i.e. is x in right field of region?
        ys = [y, y - 1, y - 2]

    for yn in ys:
        for xn in xs:
            if grid[yn][xn] == val:
                return True

    return False


def is_possible_solution(grid: GameGrid, x: int, y: int, val: int) -> bool:
    """
    Would it violate the rules to place val in the cell at (x,y)?
    """
    if (
        not is_in_row_of(grid, y, val)
        and not is_in_column_of(grid, x, val)
        and not is_in_region_of(grid, x, y, val)
    ):  # using `and not` so that cases get tested lazily
        return True

    return False


def simple_solver(grid: GameGrid) -> bool:
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for v in range(1, 10):
                    if is_possible_solution(grid, x, y, v):
                        grid[y][x] = v
                        if simple_solver(grid):
                            return True
                        grid[y][x] = 0
                return False
    return True


def remove_vals(grid: GameGrid, count: int) -> None:
    """
    Removes a given number of values from the given grid by setting them to 0.
    """
    while count != 0:
        x, y = gen_coord()
        if grid[y][x] == 0:  # if value has already been removed, try again
            continue
        grid[y][x] = 0
        count -= 1


def randomly_fill_region(grid: GameGrid, x, y) -> None:
    """
    (x,y) is the coordinate of the field in the upper-left corner of the region.
    """
    xn: int = x + 2
    yn: int = y + 2
    while y <= yn:
        while x <= xn:
            val = randint(1, 9)
            if not is_in_region_of(grid, x, y, val):
                grid[y][x] = val
                x += 1
        x -= 3
        y += 1


def randomly_fill_diagonal(grid: GameGrid) -> None:
    randomly_fill_region(grid, 0, 0)
    randomly_fill_region(grid, 3, 3)
    randomly_fill_region(grid, 6, 6)


def make_game(clue_count: int) -> GameGrid:
    """
    Makes a valid sudoku grid with the given number of clues.
    """
    game: list[list[int]] = [
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
    randomly_fill_diagonal(game)
    simple_solver(game)
    remove_count: int = (9 * 9) - clue_count
    remove_vals(game, remove_count)
    return game


if __name__ == "__main__":
    game: list[list[int]] = [
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

    # randomly_fill_diagonal(game)
    # pp(game)
    game = make_game(20)
    pp(game)
