from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__,static_folder='./static/style.css')
db = SQLAlchemy(app)
app.static_folder = 'static'
bootstrap = Bootstrap()


def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    bootstrap.init_app(app)
    db.init_app(app)

    return app
