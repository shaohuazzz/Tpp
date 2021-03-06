# 专门定义路由
from flask import Blueprint

from app.cinema.views import cinema_blue
from app.home.views import home
from app.movies.views import movies_blue
from app.user.views import user


def register_blue(app):
    app.register_blueprint(user,url_prefix='/user')
    app.register_blueprint(home,url_prefix='/home')
    app.register_blueprint(movies_blue, url_prefix='/movie')
    app.register_blueprint(cinema_blue, url_prefix='/cinema')
