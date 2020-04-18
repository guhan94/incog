from flask import (
    Flask, render_template
)
from app.config import Config
from flask_bootstrap import Bootstrap


def page_not_found(e):
    return render_template('errors/404.html'), 404


def server_error(e):
    return render_template('errors/500.html'), 500


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, server_error)

    app.config.from_object(Config)

    from . import home
    app.register_blueprint(home.bp)

    Bootstrap(app)

    return app
