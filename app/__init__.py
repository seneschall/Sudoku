import os
from flask import Flask
from .sudoku import SudokuGame
from config import HINT_COUNT

game = SudokuGame(HINT_COUNT)


def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Create and configure the app
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )

    with app.app_context():
        from . import routes  # Import routes here to avoid circular imports

    return app
