# from generator import get_column, get_region, get_row, Coordinate


# def test_get_column() -> None:
#     expected: list[Coordinate] = [
#         (0, 1),
#         (0, 2),
#         (0, 3),
#         (0, 4),
#         (0, 5),
#         (0, 6),
#         (0, 7),
#         (0, 8),
#     ]
#     assert sorted(get_column(0, 0)) == expected


# def test_get_region() -> None:
#     expected: list[Coordinate] = [
#         (0, 1),
#         (0, 2),
#         (1, 0),
#         (1, 1),
#         (1, 2),
#         (2, 0),
#         (2, 1),
#         (2, 2),
#     ]
#     assert sorted(get_region(0, 0)) == sorted(expected)
#     # assert sorted(get_region(1,1)) == expected
#     # assert sorted(get_region(2,2)) == expected


# def test_get_row() -> None:
#     expected: list[Coordinate] = [
#         (1, 0),
#         (2, 0),
#         (3, 0),
#         (4, 0),
#         (5, 0),
#         (6, 0),
#         (7, 0),
#         (8, 0),
#     ]
#     assert sorted(get_row(0, 0)) == expected
from generator import solve_naive
from classes import Game
from pprint import pp


# def test_solve_naive() -> None:
#     game = Game()
#     solve_naive(game)
#     print(game)
