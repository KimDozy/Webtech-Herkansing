import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Geheime sleutel voor sessies
    app.config['SECRET_KEY'] = 'geheimesleutel'

    # Configuratie van de database
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'login'  # Het inloggen wordt gedaan via de 'login' route

    from website.acteur.views import acteur_bp
    from website.film.views import film_bp
    from website.regisseur.views import regisseur_bp
    from website.route import main_bp

    app.register_blueprint(acteur_bp)
    app.register_blueprint(film_bp)
    app.register_blueprint(regisseur_bp)
    app.register_blueprint(main_bp)

    return app
