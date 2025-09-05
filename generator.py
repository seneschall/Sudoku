from pprint import pp

type Coordinate = tuple[int, int]


class Field:
    def __init__(self) -> None:
        # list of all possible values the field can contain
        # if value x is still possible for this field,
        # the index at x-1 is True.
        self.possible_vals: list[bool] = [True] * 9
        self.val: int = 0  # The value the field holds

    def is_possible(self, val: int) -> bool:
        """
        Checks whether the given integer is a valid value for this field.
        """
        return val in self.possible_vals

    def is_empty(self) -> bool:
        return self.val == 0

    def set(self, val) -> None:
        self.val = val
        # There are no more possible values because the value has been set:
        self.possible_vals = [False] * 9

    def add(self, val: int) -> None:
        self.possible_vals[val - 1] = True

    def remove(self, val: int) -> None:
        self.possible_vals[val - 1] = False

    def valid_vals(self) -> list[int]:
        result: list[int] = []
        for i in range(9):
            if self.possible_vals[i]:
                result.append(i + 1)
        return result

    def __str__(self) -> str:
        return str(self.possible_vals)


class Game:
    def __init__(self) -> None:
        self.grid: list[list[Field]] = (
            self.__empty_grid()
        )  # All fields are initialised to 0

    def __empty_grid(self) -> list[list[Field]]:
        """
        Generates an empty nine-by-nine grid.
        """
        row: list[Field] = []
        for _ in range(9):
            row.append(Field())

        grid: list[list[Field]] = []

        for _ in range(9):
            grid.append(row.copy())
        return grid

    def __valid_coord(self, n: int) -> bool:
        return n >= 0 and n < 9

    def clear(self) -> None:
        self.grid = self.__empty_grid()

    def get(self, x: int, y: int) -> int:
        """
        Returns the value from the grid at the xy-coordinate.
        The game board is treated as a 9x9-grid with x- and y-values going
        from 0 to 9 where (0,0) is in the upper left corner and
        (9,9) is in the lower right corner.
        """
        return self.grid[y][x].val

    def set(self, x: int, y: int, val: int) -> None:
        """
        Sets the field at the xy-coordinate to `val`.
        The game board is treated as a 9x9-grid with x- and y-values going
        from 0 to 9 where (0,0) is in the upper left corner and
        (9,9) is in the lower right corner.
        """
        self.grid[y][x].set(val)


def get_region(self, x: int, y: int) -> list[Coordinate]:
    """
    Returns a list of coordinates for all 8 fields in the same region
    as the field at coordinate (x,y).
    """
    result: list[Coordinate] = []
    # todo
    return result


def get_row(self, x: int, y: int) -> list[Coordinate]:
    """
    Returns a list of coordinates for all 8 fields in the same row
    as the field at coordinate (x,y).
    """
    result: list[Coordinate] = []
    # todo
    return result


def get_column(self, x: int, y: int) -> list[Coordinate]:
    """
    Returns a list of coordinates for all 8 fields in the same column
    as the field at coordinate (x,y).
    """
    result: list[Coordinate] = []
    # todo
    return result


if __name__ == "__main__":
    game = Game()
    game.set(0, 1, 9)
    game.set(0, 0, 1)
    pp(game.grid)
