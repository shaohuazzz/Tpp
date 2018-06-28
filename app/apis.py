# 专门定义路由
from flask import Blueprint

from app.home.views import home
from app.user.views import user


def register_blue(app):
    app.register_blueprint(user,url_prefix='/user')
    app.register_blueprint(home,url_prefix='/home')