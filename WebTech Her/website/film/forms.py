from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired

# Formulier voor het toevoegen van een Film
class VoegtoeFilm(FlaskForm):
    titel = StringField('Titel', validators=[DataRequired()])
    regisseur_id = SelectField('Regisseur', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Film Toevoegen')

    # Formulier voor het verwijderen van een Film
class VerwijderForm(FlaskForm):

    titel = StringField('Titel', validators=[DataRequired()])
    submit = SubmitField('Verwijderen')