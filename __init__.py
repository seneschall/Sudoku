import os

from flask import Flask


def create_app():
    from app import app

    return app
