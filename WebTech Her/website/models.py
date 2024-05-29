from website import db

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

class Beheerder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))

    def __repr__(self):
        return f"<Beheerder {self.username}>"
