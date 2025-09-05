from flask import (
    Flask,
    # redirect,
    render_template,
    # render_template_string,
    # request,
    # send_from_directory,
    # Response,
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
