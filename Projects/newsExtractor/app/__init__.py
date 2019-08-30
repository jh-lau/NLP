"""
  User: Liujianhan
  Time: 23:02
 """
from flask import Flask
from flask_bootstrap import Bootstrap

__author__ = 'liujianhan'

bootstrap = Bootstrap()


def creat_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    bootstrap.init_app(app)

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
