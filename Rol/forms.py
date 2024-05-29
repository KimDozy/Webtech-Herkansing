from website.models import rol
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField 
from wtforms.validators import ValidationError, DataRequired

# Formulier voor het toevoegen van een Rol
class VoegtoeInstelling(FlaskForm):

    naam = StringField("Naam van de Rol: ", validators=[DataRequired()])
  
    id = IntegerField("ID van de Rol: ", validators=[DataRequired()])
    submit = SubmitField("Toevoegen", validators=[DataRequired()])

    # Valideer of het opgegeven Rol Id bestaat
    def validate_id(self, id):
        Rol = Rol.query.get(id.data)
        if Rol is None:
            raise ValidationError('Dit rol ID bestaat niet. Voer een geldig Rol ID in.')