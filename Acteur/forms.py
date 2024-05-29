from website.models import ####
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import ValidationError, DataRequired

# Formulier voor het toevoegen van een student aan een stage
class VoegtoeStudent(FlaskForm):

    naam = StringField("Naam van de acteur: ", validators=[DataRequired()])
    id = IntegerField("ID van de acteur: ", validators=[DataRequired()])
    submit = SubmitField("Toevoegen")

    # Valideer of het opgegeven stage ID bestaat
    def validate_id(self, id):
        stage = Stage.query.get(id.data)
        if stage is None:
            raise ValidationError('Dit acteur ID bestaat niet. Voer een geldig ID in.')