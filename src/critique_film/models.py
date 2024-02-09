# SUPPIAH KAAVYA

# importer l'instanciation db de SQLAlchemy
from .database import db
from datetime import datetime

# class Auteur(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(80), nullable=False)
#     date_naissance = db.Column(db.DateTime, default=datetime.utcnow)
#     nationalite = db.Column(db.String(500), nullable=False)
#     # Relation un à plusieurs : Un auteur peut avoir plusieurs livres
#     livres = db.relationship('Livre', backref='auteur', lazy='dynamic')

# class Livre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     titre = db.Column(db.String(100), nullable=False)
#     date_publication = db.Column(db.DateTime, default=datetime.utcnow)
#     genre = db.Column(db.String(100), nullable=False)
#     id_auteur = db.Column(db.Integer, db.ForeignKey('auteur.id'))
#     # Relation un à plusieurs : Un livre peut être emprunté plusieurs livres
#     emprunts = db.relationship('Emprunt', backref='livre', lazy='dynamic')

# class Utilisateur(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.Text, nullable=False)
#     email = db.Column(db.String(80), nullable=False)
#     # Relation un à plusieurs : Un livre peut être emprunté plusieurs livres
#     emprunts = db.relationship('Emprunt', backref='utilisateur', lazy='dynamic')

#     # Relation many to many : Un utilisateur peut avoir plusieurs livres empruntés, un livre peut être emprunté plusieurs fois
#     # C'est donc implémenté par une table intermédiaire
# class Emprunt(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
#     id_livre = db.Column(db.Integer, db.ForeignKey('livre.id'))
#     date_retour = db.Column(db.DateTime, default=datetime.utcnow)
#     date_emprunt = db.Column(db.DateTime, default=datetime.utcnow)


