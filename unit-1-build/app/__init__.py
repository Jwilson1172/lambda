from flask import Flask, Blueprint, render_template, Request, redirect
from sqlite3 import connect

from web_app.models import db, migrate
from web_app.routes import home_routes


def create_app():

    app = Flask(__name__)

    # configure the database:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config[
        "SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # suppress warning messages

    db.init_app(app)
    migrate.init_app(app, db)

    #1
    app.register_blueprint(home_routes.home_routes)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
