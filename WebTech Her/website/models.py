from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from website import db

class Beheerder(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<Beheerder {self.email}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Acteur(db.Model):
    # Definities van de klasse hier
    pass

class Rol(db.Model):
    # Definities van de klasse hier
    pass

class Film(db.Model):
    # Definities van de klasse hier
    pass