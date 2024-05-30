# website/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from website.models import Beheerder

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Inloggen')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='Wachtwoorden moeten overeenkomen!')])
    pass_confirm = PasswordField('Wachtwoord bevestigen', validators=[DataRequired()])
    submit = SubmitField('Registreer!')

    # Controleert of het e-mailadres al in gebruik is
    def check_mail(self, field):
        if Beheerder.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres is al geregistreerd!')
        
    
    # Controleert of de gebruikersnaam al in gebruik is    
    def check_username(self, field):
        if Beheerder.query.filter_by(username=field.data).first():
            raise ValidationError('Deze gebruikersnaam wordt al gebruikt. Kies een andere naam!')