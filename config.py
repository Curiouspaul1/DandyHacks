import os


basedir = os.path.abspath(os.getcwd())


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('secretkey')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/dev.sqlite'
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


config = {
    "default": DevConfig,
    "development": DevConfig,
    "production": ProdConfig
}
