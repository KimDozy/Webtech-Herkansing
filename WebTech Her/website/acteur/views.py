# acteur/views.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from website import db
from website.models import Acteur
from website.acteur.forms import VoegtoeActeur, VerwijderForm

acteur_bp = Blueprint('acteur', __name__, template_folder='templates')

@login_required
@acteur_bp.route('/acttoevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeActeur()

    if form.validate_on_submit():
        naam = form.naam.data
        id = form.id.data
        
        existing_acteur = Acteur.query.filter_by(id=id).first()
        if existing_acteur:
            existing_acteur.naam = naam  
        else:
            new_acteur = Acteur(naam=naam, id=id)
            db.session.add(new_acteur)
        
        db.session.commit()
        return redirect(url_for('acteur.toevoegen'))
    
    return render_template('acteur_toevoegen.html', form=form)

@login_required
@acteur_bp.route('/actverwijderen', methods=['GET', 'POST'])
def verwijderen():
    form = VerwijderForm()

    if form.validate_on_submit():
        naam = form.naam.data
        # Additional fields as needed
        
        acteur_to_delete = Acteur.query.filter_by(naam=naam).first()
        if acteur_to_delete:
            db.session.delete(acteur_to_delete)
            db.session.commit()
            flash(f'Acteur {naam} succesvol verwijderd!', 'success')
        else:
            flash(f'Acteur {naam} niet gevonden!', 'danger')
        
        return redirect(url_for('acteur.lijst'))
    
    return render_template('acteur/acteur_verwijderen.html', form=form)