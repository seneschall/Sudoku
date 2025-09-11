# Sudoku Generator

A minimal webserver that generates valid Sudoku games and allows
you to play them by clicking on the empty fields and selecting
numbers from the drop-down menu. Only valid numbers will be shown 
(i.e. numbers that down already exist in the same row, column, or
9x9 region).

To play, start the server on localhost (port 5000), simply run
`run.py` in a Python virtual environment with all dependencies
installed. The easiest way to do this, is to install [uv](https://github.com/astral-sh/uv)
and simpy execute: `uv run run.py`. Visit `http://127.0.0.1:5000`
in your browser and enjoy the game!

The server creates an instance of the `SudokuGameGrid` class
from the `app.sudoku` module. All the game logic is handled server-side inside
that module.

Interactions between the frontend and the backend are handled with
HTMX.
