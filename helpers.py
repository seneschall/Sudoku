from random import randint
from typing import Optional

type Coordinate = tuple[int, int]


def get_region(x: int, y: int) -> list[Coordinate]:
    """
    Returns a list of coordinates for all 8 fields in the same region
    as the field at coordinate (x,y).
    The game board is treated as a 9x9-grid with x- and y-values going
    from 0 to 8 where (0,0) is in the upper left corner and
    (8,8) is in the lower right corner.
    """

    result: list[tuple[int, int]] = []

    # the grid is divided into 9 regions. To determine
    # all the other fields in the same region, we must
    # first determine where we must walk on the grid.
    #
    # There are three possible cases for both x and y:
    # each of them can be either left, right or centre
    # of their region. Let's save that as a "tuple" (not an actual
    # tuple because those are immutable):
    pos: list[Optional[int]] = [None, None]

    TOP = 0
    BOTTOM = 1
    CENTRE = 2
    LEFT = 0
    RIGHT = 1

    # where is x?
    # could be refactored using `x % 3` but I'll keep it as is for legibility
    if x == 0 or x == 3 or x == 6:
        pos[0] = LEFT
    elif x == 1 or x == 4 or x == 7:
        pos[0] = CENTRE
    else:
        pos[0] = RIGHT

    # where is y?
    if y == 0 or y == 3 or y == 6:
        pos[1] = TOP
    elif y == 1 or y == 4 or y == 7:
        pos[1] = CENTRE
    else:
        pos[1] = BOTTOM

    # Which values do we need to consider?
    if pos[0] == LEFT:
        xs = [x, x + 1, x + 2]
    elif pos[0] == CENTRE:
        xs = [x - 1, x, x + 1]
    else:
        xs = [x, x - 1, x - 2]

    if pos[1] == TOP:
        ys = [y, y + 1, y + 2]
    elif pos[1] == CENTRE:
        ys = [y - 1, y, y + 1]
    else:
        ys = [y, y - 1, y - 2]

    # Create list of all 9 permutations
    # i.e. all values in the region
    result = [(xn, yn) for xn in xs for yn in ys]

    result.remove((x, y))

    return result


def get_row(x: int, y: int) -> list[Coordinate]:
    """
    Returns a list of coordinates for all 8 fields in the same row
    as the field at coordinate (x,y).
    The game board is treated as a 9x9-grid with x- and y-values going
    from 0 to 8 where (0,0) is in the upper left corner and
    (8,8) is in the lower right corner.
    """
    return [(xn, y) for xn in range(9) if xn != x]


def get_column(x: int, y: int) -> list[Coordinate]:
    """
    Returns a list of coordinates for all 8 fields in the same column
    as the field at coordinate (x,y).
    The game board is treated as a 9x9-grid with x- and y-values going
    from 0 to 8 where (0,0) is in the upper left corner and
    (8,8) is in the lower right corner.
    """
    return [(x, yn) for yn in range(9) if yn != y]


def gen_coord() -> Coordinate:
    x = randint(0, 8)
    y = randint(0, 8)
    return (x, y)
