from website.models import Film
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired

# Formulier voor het toevoegen van een Regisseur
class VoegtoeRegisseur(FlaskForm):

    voornaam = StringField('Voornaam', validators=[DataRequired()])
    achternaam = StringField('Achternaam', validators=[DataRequired()])
    submit = SubmitField('Regisseur Toevoegen')

    # Valideer of het opgegeven Film ID bestaat
    def validate_id(self, id):
        film = Film.query.get(id.data)
        if film is None:
            raise ValidationError('Dit film ID bestaat niet. Voer een geldig film ID in.')
        
class VerwijderForm(FlaskForm):

    id = IntegerField('ID van regisseur: ', validators=[DataRequired()])
    submit = SubmitField('Verwijderen')