
from flask import Blueprint, render_template
from .forms import AjoutAuteur, LivreForm
# from werkzeug.security import generate_password_hash
from .database import db
from .models import *


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     form = InscriptionForm()
#     # opérations pour enregistrer le formulaire
#     if form.validate_on_submit():
#         # enregistrer le formulaire
#         # générer le hash du mot de passe
#         hashed_password = generate_password_hash(form.mot_de_passe.data, salt_length=8)
#         # enregistrer l'utilisateur
#         new_user = Utilisateur(
#             nom=form.nom.data,
#             email=form.email.data,
#             mot_de_passe_hash=hashed_password
#         )

#         # ajouter l'utilisateur dans la base de données
#         # Enregistrer la modification
#         db.session.add(new_user)

#         # Appliquer les modifications
#         db.session.commit()
#         return render_template('index.html')
#     return render_template('inscription.html', form=form)



# @main.route('/films')
# def films():
#     films = Film.query.all()
#     return render_template('films.html', films=films)

# @main.route('/film/<int:id>')
# def film_detail(id):
#     film = Film.query.get_or_404(id)
#     return render_template('film_detail.html', film=film)

# @main.route('/films/<int:id>/critique', methods=['GET', 'POST'])
# def film_critique(id):
#     form = CritiqueForm()
#     film = Film.query.get_or_404(id)
#     if form.validate_on_submit():
#         new_critique = Critique(
#             contenu=form.contenu.data,
#             film=film,
#         )
#         db.session.add(new_critique)
#         db.session.commit()
#         return render_template('film_detail.html', film=film)
#     return render_template('ajouter_critique.html', form=form, film=film)


@main.route('/ajouter-auteur', methods=['GET', 'POST'])
def ajouter_auteur():
    form = AjoutAuteur()
    if form.validate_on_submit():
        new_auteur = Auteur(
            nom=form.nom.data,
            nationalite=form.nationalite.data,
            date_naissance=form.date_naissance.data,
        )
        db.session.add(new_auteur)
        db.session.commit()
        return render_template('index.html')
    return render_template('ajouter_auteur.html', form=form)

@main.route('/auteurs')
def auteurs():
    auteurs = Auteur.query.all()
    return render_template('auteurs.html', auteurs=auteurs)

@main.route('/auteur/<int:id>')
def auteur_detail(id):
    auteur = Auteur.query.get_or_404(id)
    return render_template('auteur_detail.html', auteur=auteur)

@main.route('/auteur/<int:id>/livre', methods=['GET', 'POST'])
def livre_de_auteur(id):
    form = LivreForm()
    auteur = Auteur.query.get_or_404(id)
    if form.validate_on_submit():
        new_livre = Livre(
            titre=form.contenu.data,
            date_publication=form.contenu.data,
            genre=form.contenu.data,
            auteur=auteur,
        )
        db.session.add(new_livre)
        db.session.commit()
        return render_template('auteur_detail.html', auteur=auteur)
    return render_template('ajouter_livre.html', form=form, auteur=auteur)
