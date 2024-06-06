from website.models import Film
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired

# Formulier voor het toevoegen van een Rol
class VoegtoeRol(FlaskForm):
    acteur_id = SelectField('Acteur', coerce=int, validators=[DataRequired()])   
    personage = StringField('Personage', validators=[DataRequired()])
    submit = SubmitField('Rol Toevoegen')

    # Valideer of het opgegeven stage ID bestaat
    def validate_id(self, id):
        film = Film.query.get(id.data)
        if film is None:
            raise ValidationError('Dit film ID bestaat niet. Voer een geldig film ID in.')
        
class VerwijderRolForm(FlaskForm):

    acteur_id = IntegerField('ID van regisseur: ', validators=[DataRequired()])
    personage = StringField('Personage', validators=[DataRequired()])
    submit = SubmitField('Verwijderen')