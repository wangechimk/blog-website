import os


class Config:
    debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    Debug = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}
