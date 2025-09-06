from classes import Game


def gen_game() -> Game:
    result: Game = Game()

    # todo

    return result


def solve_naive(game: Game) -> None:
    for y in range(9):
        for x in range(9):
            if game.get(x, y).is_empty():
                # val: int = game.get(x, y).get_first_valid_val()
                for val in range(1, 10):
                    if game.get(x, y).is_possible(val):
                        game.set_and_apply_rules(x, y, val)
                        solve_naive(game)
                        game.reset_field(x, y)
                return
    return
