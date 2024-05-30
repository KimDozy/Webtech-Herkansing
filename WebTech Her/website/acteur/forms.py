# acteur/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class VoegtoeActeur(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired()])
    id = IntegerField('ID', validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

class VerwijderForm(FlaskForm):

    id = IntegerField('ID van Acteur: ', validators=[DataRequired()])
    submit = SubmitField('Verwijderen')