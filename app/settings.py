import uuid


class Config:
    DEBUG = False
    SECRET_KEY = '53534436'


def get_db_url(database:dict):
    db = database.get('DB') or 'mysql'
    user = database.get('USER') or 'root'
    password = database.get('PASSWORD') or '123456'
    host = database.get('HOST') or '127.0.0.1'
    port = database.get('PORT') or '3306'
    name = database.get('NAME')
    driver = database.get('DRIVER') or 'pymysql'
    charest = database.get('CHARSET') or 'utf8'
    return "{}+{}://{}:{}@{}:{}/{}?charset={}".format(db,driver,user,password,host,port,name,charest)

class ProductConfig(Config):
    DEBUG = False
    DATABASES = {
        'DB': 'mysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'flask',
        'DRIVER': 'pymysql',
        'CHARSET': 'utf8',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASES)

class DevelopConfig(Config):
    DEBUG = True
    DATABASES = {
        'DB': 'mysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'flask',
        'DRIVER': 'pymysql',
        'CHARSET': 'utf8',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASES)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = '18971367155@163.com'
    MAIL_PASSWORD = 'a123456'


env = {
    'dev' : DevelopConfig,
    'pro' : ProductConfig,
}