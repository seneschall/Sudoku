from flask import current_app, render_template, redirect, request
from typing import Optional
from .exceptions import InvalidFieldValue
from . import game


## general routes
@current_app.route("/generate", methods=["GET", "POST"])
def generate():
    """
    Generates a new random sudoku game and redirects to `index()`.
    """
    game.regenerate()
    return redirect("/")


@current_app.route("/", methods=["GET", "POST"])
def index():
    """
    Renders the sudoku game.
    """
    return render_template("index.html", game=game)


## HTMX routes
@current_app.route("/change_<int:x>_<int:y>", methods=["POST"])
def change(x: int, y: int):
    """
    Gets called by HTMX whenever a `select` field from the sudoku grid is changed.
    It swaps the contents of the table with the `sudoku-grid` class-label
    and replaces it with a newly rendered grid with updated grid state.
    """
    val: Optional[str] = request.form.get("value")
    if val is None:
        raise InvalidFieldValue()
    game.set_val_at(x, y, int(val))
    return render_template("sudoku_grid.html", game=game)
