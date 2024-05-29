from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from website.models import Beheerder
from website.forms import LoginForm, RegistrationForm
from website import db
from werkzeug.security import generate_password_hash, check_password_hash

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('welkom.html') # Reendert de welkompagina

@main_bp.route('/welkom')
@login_required
def welkom():
    return render_template('welkom.html') # Rendert welkom voor ingelogde gebruikers

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent uitgelogd') # Flashbericht bij uitloggen
    return redirect(url_for('main.welkom'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Beheerder.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Succesvol ingelogd.') # Flashbericht bij succesvol inloggen

            next_page = request.args.get('next')

            if not next_page or not next_page.startswith('/'):
                next_page = url_for('main.welkom')

            return redirect(next_page)

    return render_template('login.html', form=form) # Rendert inlogformulier

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = Beheerder(email=form.email.data,
                         username=form.username.data,
                         password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash('Dank voor de registratie. Er kan nu ingelogd worden !') # Flashbericht voor succesvolle registratie
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form) # Rendert het registratieformulier

@main_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 # Rendert de 404-pagina wanneer een pagina niet gevonden is
