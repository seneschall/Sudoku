from flask import (
    Flask,
    redirect,
    # redirect,
    render_template,
    render_template_string,
    # render_template_string,
    request,
    # send_from_directory,
    # Response,
)

from sudoku import GameGrid, SudokuGame

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
    grid: GameGrid = game.grid
    possible_vals = game.possible_vals
    return render_template("index.html", grid=grid, possible_vals=possible_vals)


## HTMX routes
@app.route("/possible_at_<int:x>_<int:y>")
def possible_at(x: int, y: int):
    possible_vals: list[int] = game.get_possible_vals_at(x, y)
    return render_template("possible_vals.html", possible_vals=possible_vals, x=x, y=y)


@app.route("/val_changed_at_<int:x>_<int:y>", methods=["POST"])
def val_changed(x: int, y: int):
    val = request.form.get("value")
    return render_template_string("{{val}}", val=val)


if __name__ == "__main__":
    app.run(debug=True)
