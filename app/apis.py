# 专门定义路由
from flask import Blueprint

from app.user.views import user


def register_blue(app):
    app.register_blueprint(user,url_prefix='/user')