# film/views.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from website import db
from website.models import Film
from website.film.forms import VoegtoeFilm, VerwijderForm

film_bp = Blueprint('film', __name__, template_folder='templates/film')

@login_required
@film_bp.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeFilm()

    if form.validate_on_submit():
        titel = form.titel.data
        # Voeg andere velden toe zoals nodig
        
        new_film = Film(titel=titel)
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for('film.lijst'))
    
    return render_template('toevoegen_film.html', form=form)


@login_required
@film_bp.route('/verwijderen', methods=['GET', 'POST'])
def verwijderen():
    form = VerwijderForm()

    if form.validate_on_submit():
        titel = form.titel.data
        # Voeg andere velden toe zoals nodig
        
        new_film = Film(titel=titel)
        db.session.delete(new_film)
        db.session.commit()
        return redirect(url_for('film.lijst'))
    
    return render_template('toevoegen_film.html', form=form)


@film_bp.route('/lijst')
def lijst():
    films = Film.query.all()
    return render_template('film_lijst.html', films=films)
