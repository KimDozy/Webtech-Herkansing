from website import db, app, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Methode om gebruikers op te halen aan de hand van hun ID voor inlogbeheer
@login_manager.user_loader
def load_user(user_id):
    return Beheerder.query.get(user_id)


# Model voor Beheerder (administrator) met authenticatiefunctionaliteit
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


# Model voor Regisseur met betrekking tot Films
class Regisseur(db.Model):
    __tablename__ = 'regisseurs'
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)
    film = db.relationship('Film', backref='regisseur', lazy=True)

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam


# Model voor Acteur
class Acteur(db.Model):
    __tablename__ = 'acteurs'
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)
    rollen = db.relationship('Rol', backref='acteur', lazy=True)

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam



# Model voor Film
class Film(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.Text)
    regisseur_id = db.Column(db.Integer, db.ForeignKey('regisseur.id'), nullable=False)
    rol = db.relationship('Rol', backref='films', uselist=False, cascade='all, delete-orphan')

    def __init__(self, titel, regisseur_id):
        self.naam = titel
        self.regisseur_id = regisseur_id


# Model voor Rol
class Rol(db.Model):
    __tablename__ = 'rollen'
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    acteur_id = db.Column(db.Integer, db.ForeignKey('acteur.id'), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)

    def __init__(self, naam, acteur_id, film_id):
        self.naam = naam
        self.acteur_id = acteur_id
        self.film_id = film_id


# Creëert de database tabellen
with app.app_context():
    db.create_all()