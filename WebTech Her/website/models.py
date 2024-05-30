from website import db, app, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Acteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100))

    def __repr__(self):
        return f"<Acteur {self.naam}>"

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personage = db.Column(db.String(100))
    acteur_id = db.Column(db.Integer, db.ForeignKey('acteur.id'))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))

    acteur = db.relationship('Acteur', backref='rollen')

    def __repr__(self):
        return f"<Rol {self.personage}>"

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(100))
    regisseur_id = db.Column(db.Integer, db.ForeignKey('regisseur.id'))

    regisseur = db.relationship('Regisseur', backref='films')

    def __repr__(self):
        return f"<Film {self.titel}>"


class Regisseur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100))

    def __repr__(self):
        return f"<Regisseur {self.naam}>"

class Beheerder(db.Model, UserMixin):
    __tablename__ = 'beheerders'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return Beheerder.query.get(user_id)

with app.app_context():
    db.create_all()