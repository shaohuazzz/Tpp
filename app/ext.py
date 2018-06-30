import os

from flask_caching import Cache
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import  SQLAlchemy


def init_ext(app):
   init_db(app)
   init_mail(app)
   init_cache_config(app)
   init_marshmallow(app)


db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    db.init_app(app=app)
    migrate.init_app(app, db)

mail = Mail()

def init_mail(app):
    mail.init_app(app)

cache = Cache(config={'CACHE_TYPE': 'redis'})

def init_cache_config(app):
    cache.init_app(app)



ma = Marshmallow()
def init_marshmallow(app):
    ma.init_app(app)