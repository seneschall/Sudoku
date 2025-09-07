# from sudoku import simple_solver
from sudoku import is_in_column_of, is_in_region_of, is_in_row_of


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
