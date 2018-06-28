from flask import Flask
from flask_cors import CORS

from app.apis import register_blue
from app.ext import init_ext
from app.settings import env
from app import settings

app = Flask(__name__)
CORS(app,)
def create_app(env_name):

    app.config.from_object(env.get(env_name))
    init_ext(app)
    register_blue(app)
    return app