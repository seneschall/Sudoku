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

from sudoku import make_game

app = Flask(__name__)

grid: list[list[int]] = []


@app.route("/generate", methods=["GET", "POST"])
def gen():
    global grid
    grid = make_game(20)
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", grid=grid)


if __name__ == "__main__":
    grid = make_game(20)
    app.run(debug=True)
