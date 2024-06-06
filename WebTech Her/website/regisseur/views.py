# regisseur/views.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from website import db
from website.models import Regisseur
from website.regisseur.forms import VoegtoeRegisseur, VerwijderForm

regisseur_bp = Blueprint('regisseur', __name__, template_folder='templates')

@login_required
@regisseur_bp.route('/regtoevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeRegisseur()

    if form.validate_on_submit():
        voornaam = form.voornaam.data
        achternaam = form.achternaam.data
        # Voeg andere velden toe zoals nodig
        
        new_regisseur = Regisseur(voornaam=voornaam, achternaam=achternaam)
        db.session.add(new_regisseur)
        db.session.commit()
        return redirect(url_for('regisseur.lijst'))
    
    return render_template('regisseurs_toevoegen.html', form=form)

@login_required
@regisseur_bp.route('/regverwijderen', methods=['GET', 'POST'])
def verwijderen():
    form = VerwijderForm()

    if form.validate_on_submit():
        id = form.id.data
        # Voeg andere velden toe zoals nodig
        
        new_regisseur = Regisseur(id=id)
        db.session.delete(new_regisseur)
        db.session.commit()
        return redirect(url_for('regisseur.lijst'))
    
    return render_template('regisseur_verwijderen.html', form=form)

@regisseur_bp.route('/reglijst')
def lijst():
    regisseurs = Regisseur.query.all()
    return render_template('regisseurs.html', regisseurs=regisseurs)
