from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from markupsafe import Markup
from website.models import Acteur, Rol, Film
from website.acteur.forms import VoegtoeActeur
from website import db

acteur_bp = Blueprint('acteur', __name__, template_folder='templates/Acteur')

@login_required
@acteur_bp.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeActeur()
    if form.validate_on_submit():
        naam = form.naam.data
        id = form.id.data
        
        existing_acteur = Acteur.query.filter_by(id=id).first()
        if existing_acteur:
            existing_acteur.naam = naam
        else:
            new_acteur = Acteur(naam=naam, film_id=id)
            db.session.add(new_acteur)
        
        db.session.commit()
        return redirect(url_for('acteur.lijst'))
    
    return render_template('acteur_toevoegen.html', form=form)

@login_required
def acteur_delete(id):
    acteur = Acteur.query.get_or_404(id)
    roles = Rol.query.filter_by(acteur_id=id).all()

    if roles:
        roles_info = "<br>- " + "<br>- ".join([f"'{rol.personage}' in '{Film.query.get(rol.film_id).titel}'" for rol in roles])
        flash(Markup(f'Cannot delete actor because they are assigned to roles:<br>{roles_info}'), 'danger')
        return redirect(url_for('acteur.acteurs'))
    else:
        db.session.delete(acteur)
        db.session.commit()
        flash('Actor successfully deleted', 'success')
        return redirect(url_for('acteur.acteurs'))
