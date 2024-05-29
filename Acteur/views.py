from flask import Blueprint, render_template, redirect, url_for, flash
from website import db
from website.models import acteur
from website.acteur.forms import Voegtoeacteur

# Definiëren van de studenten blueprint met bijbehorende URL-prefix en template folder
studenten_blueprint = Blueprint('acteur',
                                __name__,
                                template_folder='templates/Acteur')

# Route voor het toevoegen van een student
@studenten_blueprint.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeStudent()

    if form.validate_on_submit():
        naam = form.naam.data
        id = form.id.data
        
        # Controleren of de student al bestaat op basis van ID
        existing_acteur = acteur.query.filter_by(id=id).first()
        if existing_acteur:
            existing_acteur.naam = naam  # Naam bijwerken als de student al bestaat
        else:
            new_acteur = acteur(naam=naam, stage_id=id)
            db.session.add(new_acteur)
        
        db.session.commit()
        return redirect(url_for('acteur.lijst')) # Doorverwijzen naar de lijst met stages na toevoegen van student
    
    return render_template('acteur_toevoegen.html', form=form)
