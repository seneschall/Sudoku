from flask import (
    Flask,
    redirect,
    # redirect,
    render_template,
    # render_template_string,
    # request,
    # send_from_directory,
    # Response,
)

from sudoku import GameGrid, SudokuGame

app = Flask(__name__)

game: SudokuGame = SudokuGame()  # game-state is stored on server in "singleton"


@app.route("/generate", methods=["GET", "POST"])
def gen():
    global game
    game.regenerate()
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
    grid: GameGrid = game.grid
    return render_template("index.html", grid=grid)


if __name__ == "__main__":
    app.run(debug=True)
