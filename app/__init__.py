from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
db = SQLAlchemy(app)
app.static_folder = 'static'
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.load_view = 'auth.login'
login_manager.login_message_category = 'info'
mail = Mail(app)
login_manager.init_app(app)


def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    return app
