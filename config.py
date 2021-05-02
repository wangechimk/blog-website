import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql+psycopg2://michellewangechi:Rosemary70@localhost/blogwebsite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '1234key')
    UPLOADED_PHOTOS_DEST = 'app/static/img'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

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
