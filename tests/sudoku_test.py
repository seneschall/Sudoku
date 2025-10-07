from random import randint
from app.sudoku import (
    is_in_column_of,
    is_in_region_of,
    is_in_row_of,
    make_game,
    is_possible_solution,
    randomly_fill_diagonal,
    simple_solver
)


def test_is_possible_solution() -> None:
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert is_possible_solution(grid, 0, 1, 4) is False
    assert is_possible_solution(grid, 0, 1, 5) is False
    assert is_possible_solution(grid, 0, 1, 1) is True
    assert is_possible_solution(grid, 1, 3, 5) is True


def test_is_in_region_of() -> None:
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert is_in_region_of(grid, 0, 0, 1) is False
    assert is_in_region_of(grid, 0, 0, 4) is True
    assert is_in_region_of(grid, 4, 1, 1) is True
    assert is_in_region_of(grid, 8, 8, 8) is True
    assert is_in_region_of(grid, 4, 8, 2) is True
    assert is_in_region_of(grid, 4, 8, 8) is False


def test_is_in_row_of() -> None:
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert is_in_row_of(grid, 1, 4) is True
    assert is_in_row_of(grid, 1, 3) is False
    assert is_in_row_of(grid, 2, 5) is True
    assert is_in_row_of(grid, 7, 8) is True
    assert is_in_row_of(grid, 7, 7) is False


def test_is_in_column_of() -> None:
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert is_in_column_of(grid, 1, 4) is True
    assert is_in_column_of(grid, 1, 3) is True
    assert is_in_column_of(grid, 3, 9) is True
    assert is_in_column_of(grid, 3, 2) is True
    assert is_in_column_of(grid, 8, 3) is False
    assert is_in_column_of(grid, 2, 5) is False


def test_make_game() -> None:
    def count_zeros(game: list[list[int]]) -> int:
        count: int = 0
        for row in game:
            for val in row:
                if val == 0:
                    count += 1
        return count

    TOTAL_COUNT = 81
    game = make_game(18)
    assert count_zeros(game) == TOTAL_COUNT - 18
    game = make_game(80)
    assert count_zeros(game) == TOTAL_COUNT - 80
    game = make_game(0)
    assert count_zeros(game) == TOTAL_COUNT

    # testing for solvability of generated games
    for i in range(100):
        num: int = randint(20, 80)
        game = make_game(num)
        simple_solver(game) # if not solvable, will get stuck in infinite loop


def test_randomly_fill_diagonal() -> None:
    def region_is_empty(grid: list[list[int]], x: int, y: int) -> bool:
        """
        (x,y) is upper-left corner of region.
        True if every field in region is set to 0.
        """
        for yn in range(y, y + 3):
            for xn in range(x, x + 3):
                if grid[yn][xn] != 0:
                    return False
        return True

    def region_is_filled(grid: list[list[int]], x: int, y: int) -> bool:
        """
        (x,y) is upper-left corner of region.
        True if no field in region is set to 0.
        """
        for yn in range(y, y + 3):
            for xn in range(x, x + 3):
                if grid[yn][xn] == 0:
                    return False
        return True

    def test() -> None:
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
        assert (
            region_is_filled(game, 0, 0)
            and region_is_filled(game, 3, 3)
            and region_is_filled(game, 6, 6)
            and region_is_empty(game, 3, 0)
            and region_is_empty(game, 6, 0)
            and region_is_empty(game, 0, 3)
            and region_is_empty(game, 6, 3)
            and region_is_empty(game, 0, 6)
            and region_is_empty(game, 3, 6)
        )

    test()
    test()
    test()
    test()
    test()
    test()


# def test_simple_solver() -> None:
#     grid: list[list[int]] = [
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     ]
