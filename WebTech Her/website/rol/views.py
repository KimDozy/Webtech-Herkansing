from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from website import db
from website.models import Rol
from website.rol.forms import VoegtoeRol, VerwijderRolForm

rol_bp = Blueprint('rol', __name__, template_folder='templates/rol')

@login_required
@rol_bp.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeRol()

    if form.validate_on_submit():
        naam = form.naam.data
        id = form.id.data
        
        existing_rol = Rol.query.filter_by(id=id).first()
        if existing_rol:
            existing_rol.naam = naam  
        else:
            new_rol = Rol(naam=naam, id=id)
            db.session.add(new_rol)
        
        db.session.commit()
        flash(f'Rol {naam} succesvol toegevoegd!', 'success')
        return redirect(url_for('rol.lijst'))
    
    return render_template('toevoegen_rol.html', form=form)

@login_required
@rol_bp.route('/verwijderen', methods=['GET', 'POST'])
def verwijderen():
    form = VerwijderRolForm()

    if form.validate_on_submit():
        naam = form.naam.data
        # Voeg andere velden toe zoals nodig
        
        new_rol = Rol(naam=naam)
        db.session.delete(new_rol)
        db.session.commit()
        return redirect(url_for('rol.lijst'))
    
    return render_template('rol_verwijderen.html', form=form)

@login_required
@rol_bp.route('/lijst', methods=['GET'])
def lijst():
    rollen = Rol.query.all()
    return render_template('lijst_rol.html', rollen=rollen)
