from helpers import get_column, get_row, get_region

type Coordinate = tuple[int, int]


class Field:
    def __init__(self) -> None:
        # list of all possible values the field can contain
        # if value x is still possible for this field,
        # the index at x-1 is True.
        # We need to store this so we can display a list
        # of all possible values to the player.
        self.possible_vals: list[bool] = [True for _ in range(9)]
        self.val: int = 0  # The value the field holds

    def __str__(self) -> str:
        # return str(self.possible_vals)
        return str(self.val)

    def is_possible(self, val: int) -> bool:
        """
        Checks whether the given integer is a valid value for this field.
        """
        return self.possible_vals[val - 1]

    def is_empty(self) -> bool:
        return self.val == 0

    def set(self, val: int) -> None:
        self.val = val
        # # There are no more possible values because the value has been set:
        # self.possible_vals = [False] * 9

    def add(self, val: int) -> None:
        """
        Adds `val` to `possible_vals`.
        """
        self.possible_vals[val - 1] = True

    def remove(self, val: int) -> None:
        """
        Removes `val` from `possible_vals`.
        """
        self.possible_vals[val - 1] = False

    def get_first_valid_val(self) -> int:
        for i in range(9):
            if self.possible_vals[i]:
                return i + 1
        return 0  # i.e. no valid value found

    def valid_vals(self) -> list[int]:
        result: list[int] = []
        for i in range(9):
            if self.possible_vals[i]:
                result.append(i + 1)
        return result

    def num_of_possible_vals(self) -> int:
        """
        Returns the number of possible values for this field.
        """
        return len([x for x in self.possible_vals if x])


class Game:
    def __init__(self) -> None:
        self.grid: list[list[Field]] = (
            self.__empty_grid()
        )  # All fields are initialised to 0

    def __str__(self) -> str:
        result = "\n"
        for row in self.grid:
            lst: list[str] = []
            for f in row:
                val = f.val
                lst.append(str(val))
            result += " ".join(lst) + "\n"

        return result

    def __empty_grid(self) -> list[list[Field]]:
        """
        Generates an empty nine-by-nine grid.
        """
        grid: list[list[Field]] = []

        for _ in range(9):
            row: list[Field] = []
            for _ in range(9):
                row.append(Field())
            grid.append(row)
        return grid

    def clear(self) -> None:
        self.grid = self.__empty_grid()

    def get(self, x: int, y: int) -> Field:
        """
        Returns the value from the grid at the xy-coordinate.
        The game board is treated as a 9x9-grid with x- and y-values going
        from 0 to 9 where (0,0) is in the upper left corner and
        (9,9) is in the lower right corner.
        """
        return self.grid[y][x]

    def set_and_apply_rules(self, x: int, y: int, val: int) -> None:
        """
        Sets the field at the xy-coordinate to `val`.
        The game board is treated as a 9x9-grid with x- and y-values going
        from 0 to 8 where (0,0) is in the upper left corner and
        (8,8) is in the lower right corner.
        """
        self.grid[y][x].set(val)

        # now we need to find all fields affected by this change
        col = get_column(x, y)
        row = get_row(x, y)
        region = get_region(x, y)

        # and then remove the possible values appropriately
        for xf, yf in col:
            f: Field = self.get(xf, yf)
            f.remove(val)

        for xf, yf in row:
            f: Field = self.get(xf, yf)
            f.remove(val)

        for xf, yf in region:
            f: Field = self.get(xf, yf)
            f.remove(val)

    def reset_field(self, x: int, y: int) -> None:
        """
        Readds the value from (x,y) to all fields in the same region, row, or column
        as (x,y), and resets the field at (x,y).
        """
        val = self.get(x, y).val
        col = get_column(x, y)
        row = get_row(x, y)
        region = get_region(x, y)

        # and then remove the possible values appropriately
        for xf, yf in col:
            f: Field = self.get(xf, yf)
            f.add(val)

        for xf, yf in row:
            f: Field = self.get(xf, yf)
            f.add(val)

        for xf, yf in region:
            f: Field = self.get(xf, yf)
            f.add(val)

        self.get(x, y).set(0)

    def apply_rules_to_entire_grid(self) -> None:
        """
        This is to ensure that the grid remains valid after backtracking.
        """
        # Iterate over entire grid. If a value is set, make sure
        # it's not in the possible_values for any fields where it shouldn't be.
        for x in range(9):
            for y in range(9):
                val = self.get(x, y).val

                if val == 0:
                    continue

                col = get_column(x, y)
                row = get_row(x, y)
                region = get_region(x, y)

                # and then remove the possible values appropriately
                for xf, yf in col:
                    f: Field = self.get(xf, yf)
                    f.remove(val)

                for xf, yf in row:
                    f: Field = self.get(xf, yf)
                    f.remove(val)

                for xf, yf in region:
                    f: Field = self.get(xf, yf)
                    f.remove(val)


if __name__ == "__main__":
    game = Game()
    game.set_and_apply_rules(1, 3, 5)
    game.set_and_apply_rules(0, 0, 1)
    print(game)
