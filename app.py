from typing import Optional
from flask import (
    Flask,
    redirect,
    render_template,
    request,
)

from exceptions import InvalidFieldValue
from sudoku import SudokuGame

app = Flask(__name__)

game: SudokuGame = SudokuGame()  # game-state is stored on server in "singleton"


# routes


## general routes
@app.route("/generate", methods=["GET", "POST"])
def gen():
    game.regenerate()
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", game=game)


## HTMX routes
@app.route("/change_<int:x>_<int:y>", methods=["POST"])
def change(x: int, y: int):
    val: Optional[str] = request.form.get("value")
    if val is None:
        raise InvalidFieldValue(val)
    game.set_val_at(x, y, int(val))
    return render_template("sudoku_grid.html", game=game)


if __name__ == "__main__":
    app.run(debug=True)
