from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email


# class InscriptionForm(FlaskForm):
#     nom = StringField('Nom', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
#     submit = SubmitField('Inscription')


class AjoutAuteur(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    date_naissance = DateField('date', validators=[DataRequired()])
    nationalite = StringField('nationalite', validators=[DataRequired()])
    submit = SubmitField('Ajouter')

    
class AjoutLivre(FlaskForm):
    titre = StringField('titre', validators=[DataRequired()])
    date_publication = DateField('date', validators=[DataRequired()])
    genre = StringField('nationalite', validators=[DataRequired()])
    id_auteur = IntegerField('id_auteur', validators=[DataRequired()])
    submit = SubmitField('Ajouter')


# class CritiqueForm(FlaskForm):
#     contenu = TextAreaField('Critique', validators=[DataRequired()])
#     submit = SubmitField('Publier')


class LivreForm(FlaskForm):
    titre = StringField('titre', validators=[DataRequired()])
    date_publication = DateField('date', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    auteur = StringField('auteur', validators=[DataRequired()])
    submit = SubmitField('Ajouter')

