import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

# Geheime sleutel voor sessies
app.config['GEHEIME_SLEUTEL'] = 'geheimesleutel'

# Configuratie van de database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'geheimesleutel' # Geheime sleutel voor sessies

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)

login_manager.login_view = 'login' # Het inloggen wordt gedaan via de 'login' route

# from website import route
# from website import models

# Importeren van blueprints voor de verschillende onderdelen van de website
# from website.stage.views import stages_blueprint
# from website.student.views import studenten_blueprint
# from website.begeleider.views import begeleiders_blueprint
# from website.instelling.views import instellingen_blueprint

# # Registreren van de blueprints met hun respectievelijke URL-prefixes
# app.register_blueprint(stages_blueprint, url_prefix='/stages')
# app.register_blueprint(studenten_blueprint, url_prefix='/studenten')
# app.register_blueprint(begeleiders_blueprint, url_pefix='/begeleiders')
# app.register_blueprint(instellingen_blueprint, url_prefix='/instellingen')