from flask import Blueprint, render_template, redirect, url_for
from website import db
from website.models import Instelling
from website.rol.forms import VoegtoeInstelling

instellingen_blueprint = Blueprint('instellingen',
                                   __name__,
                                   template_folder="templates/instellingen")

# Route voor het toevoegen van een ID
@instellingen_blueprint.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeInstelling()

    if form.validate_on_submit():
        naam = form.naam.data
        
        id = form.id.data
        
    
        existing_rol = new_rol.query.filter_by(id=id).first()
        if existing_rol:
            existing_rol.naam = naam  # Naam bijwerken als de instelling al bestaat
           
        else:
            new_rol = rol(naam=naam, stage_id=id)
            db.session.add(Naam_rol) #WE MOETEN EEN ROL IN DE DATABASE AANMAKEN
        
        db.session.commit()
        return redirect(url_for('rol.lijst')) # Doorverwijzen naar de lijst met id's 
    
    return render_template('Rol_toevoegen.html', form=form)
