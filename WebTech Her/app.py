# app.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from website import app  # Import Flask app
from website.route import *  # Import routes van route.py

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Geheime sleutel voor sessies
    app.config['SECRET_KEY'] = 'geheimesleutel'

    # Configuratie van de database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'login'  # Het inloggen wordt gedaan via de 'login' route

    from website.acteur.views import acteur_bp
    from website.film.views import film_bp
    from website.regisseur.views import regisseur_bp

    app.register_blueprint(acteur_bp)
    app.register_blueprint(film_bp)
    app.register_blueprint(regisseur_bp)

    return app

if __name__ == '__main__':
    app.run(debug=True)