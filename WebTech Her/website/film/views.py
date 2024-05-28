import os
import secrets
from flask import Blueprint, current_app, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from website.film.forms import VoegtoeFilm, RolForm
from website.models import Acteur, Film, Regisseur, Rol
from app import db

film_bp = Blueprint('film', __name__, url_prefix='/film')



@film_bp.route('/<int:id>', methods=['GET'])
def film_detail(id):
    film: Film = Film.query.get_or_404(id) 
    rollen = Rol.query.join(Acteur).filter(Rol.film_id==id).all()
    
    return render_template('film/film_detail.html', film=film, rollen=rollen)

   
@film_bp.route('/add', methods=['GET', 'POST'])
@login_required
def film_add():
    form: VoegtoeFilm = VoegtoeFilm()
    form.regisseur_id.choices = [(0, 'Choose...')] + [(r.id, r.voornaam + ' '  + r.achternaam) for r in Regisseur.query.all()]


@film_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_film(id):
    film:Film = Film.query.get_or_404(id)
    form:VoegtoeFilm = VoegtoeFilm(obj=film)

    form.regisseur_id.choices = [(0, 'Choose...')] + [(r.id, r.voornaam + ' ' + r.achternaam) for r in Regisseur.query.all()]

    if form.validate_on_submit():
        film.titel = form.titel.data
        film.regisseur_id = form.regisseur_id.data
        
        db.session.commit()
        flash('De film is succesvol bijgewerkt!', 'success')
        return redirect(url_for('film.film_detail', id=film.id))
    
    return render_template('film/film_edit.html', form=form, film=film)



@film_bp.route('/delete/<int:id>')
@login_required
def delete_film(id):
    film:Film = Film.query.get_or_404(id)
    
    # Delete associated roles
    Rol.query.filter_by(film_id=id).delete()

    # Delete the film
    db.session.delete(film)
    db.session.commit()
    flash('Film successfully deleted.', 'success')
    return redirect(url_for('main.index'))

# ROL FILM

@film_bp.route('/rol/add/<int:film_id>', methods=['GET', 'POST'])  # New route to handle specific film ID
@login_required
def rol_add(film_id):
    form:RolForm = RolForm()
    form.acteur_id.choices = [(0, 'Choose...')] + [(a.id, a.voornaam + ' ' + a.achternaam) for a in Acteur.query.all()]

    if form.validate_on_submit():
        rol:Rol = Rol(
            acteur_id=form.acteur_id.data, 
            film_id=film_id,
            personage=form.personage.data
        )
        db.session.add(rol)
        db.session.commit()
        flash('De Rol is succesvol toegevoegd!', 'success')
        return redirect(url_for('film.film_detail', id=film_id, tab='actors-roles'))
    
    return render_template('film/film_rol_add.html', form=form, film_id=film_id)


@film_bp.route('/rol/edit/<int:id>', methods=['GET', 'POST'])
@login_required  
def rol_edit(id):
    rol:Rol = Rol.query.get_or_404(id)
    form:RolForm = RolForm(obj=rol)
    
    # Update choices for acteur_id
    form.acteur_id.choices = [(0, 'Choose...')] +  [(acteur.id, acteur.voornaam + ' ' + acteur.achternaam) for acteur in Acteur.query.order_by(Acteur.voornaam).all()]
    
    if request.method == 'POST' and form.validate_on_submit():
        rol.acteur_id = form.acteur_id.data
        rol.personage = form.personage.data
        db.session.commit()
        flash('Rol successfully updated!', 'success')
        return redirect(url_for('film.film_detail', id=rol.film_id, tab='actors-roles'))
    
    return render_template('film/film_rol_edit.html', form=form, rol=rol)


@film_bp.route('/rol/delete/<int:id>', methods=['GET'])
@login_required
def rol_delete(id):
    rol:Rol = Rol.query.get_or_404(id)
    film_id = rol.film_id
    db.session.delete(rol)
    db.session.commit()
    flash('De Rol is succesvol verwijderd!', 'success')
    return redirect(url_for('film.film_detail', id=film_id, tab='actors-roles'))