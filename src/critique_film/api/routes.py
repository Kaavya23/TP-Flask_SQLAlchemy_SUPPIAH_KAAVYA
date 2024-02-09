from flask import Blueprint, jsonify, request
from ..models import Chambre, Reservation, Client
from .. import db
from datetime import datetime

main = Blueprint('api', __name__)

@main.route('/api/chambres', methods=['POST'])
def ajouter_chambre():
    data = request.json
    numero = data.get('numero')
    type_chambre = data.get('type')
    prix = data.get('prix')

    if not numero or not type_chambre or not prix:
        return jsonify({"success": False, "message": "Veuillez fournir toutes les informations nécessaires."}), 400

    chambre_existe = Chambre.query.filter_by(numero=numero).first()
    if chambre_existe:
        return jsonify({"success": False, "message": "Le numéro de chambre existe déjà."}), 400

    nouvelle_chambre = Chambre(numero=numero, type=type_chambre, prix=prix)

    db.session.add(nouvelle_chambre)
    db.session.commit()

    return jsonify({"success": True, "message": "Chambre ajoutée avec succès."}), 201


@main.route('/api/chambres/<int:id>', methods=['PUT'])
def modifier_chambre(id):
    chambre = Chambre.query.get_or_404(id)

    data = request.json
    numero = data.get('numero')
    type_chambre = data.get('type')
    prix = data.get('prix')

    chambre.numero = numero
    chambre.type = type_chambre
    chambre.prix = prix

    db.session.commit()

    return jsonify({"success": True, "message": "Chambre mise à jour avec succès."})


@main.route('/api/chambres/<int:id>', methods=['DELETE'])
def supprimer_chambre(id):
    chambre = Chambre.query.get_or_404(id)

    db.session.delete(chambre)
    db.session.commit()

    return jsonify({"success": True, "message": "Chambre supprimée avec succès."})

@main.route('/api/chambres/disponibles', methods=['GET'])
def chambres_disponibles():
    date_arrivee = request.args.get('date_arrivee')
    date_depart = request.args.get('date_depart')

    if not date_arrivee or not date_depart:
        return jsonify({"message": "Veuillez fournir les dates d'arrivée et de départ"}), 400

    chambres_disponibles = Chambre.query.filter(
        ~Chambre.reservations.any(
            (Reservation.date_arrivee <= date_depart) &
            (Reservation.date_depart >= date_arrivee)
        )
    ).all()

    if not chambres_disponibles:
        return jsonify({"message": "Aucune chambre disponible pour les dates spécifiées."}), 404

    result = []
    for chambre in chambres_disponibles:
        result.append({
            "id": chambre.id,
            "numero": chambre.numero,
            "type": chambre.type,
            "prix": chambre.prix
        })

    return jsonify(result), 200


@main.route('/api/reservations', methods=['POST'])
def creer_reservation():
    data = request.json
    id_client = data.get('id_client')
    id_chambre = data.get('id_chambre')
    date_arrivee = data.get('date_arrivee')
    date_depart = data.get('date_depart')
    statut = "Confirmée"

    if not id_client or not id_chambre or not date_arrivee or not date_depart:
        return jsonify({"success": False, "message": "Veuillez fournir toutes les données nécessaires."}), 400

    reservations_existantes = Reservation.query.filter(
        (Reservation.id_chambre == id_chambre) &
        ((Reservation.date_arrivee <= date_depart) & (Reservation.date_depart >= date_arrivee))
    ).all()

    if reservations_existantes:
        return jsonify({"success": False, "message": "La chambre n'est pas disponible pour les dates demandées."}), 400

    nouvelle_reservation = Reservation(id_client=id_client, id_chambre=id_chambre, date_arrivee=date_arrivee, date_depart=date_depart, statut=statut)
    db.session.add(nouvelle_reservation)
    db.session.commit()

    return jsonify({"success": True, "message": "Réservation créée avec succès."}), 201


@main.route('/api/reservations/<int:id>', methods=['DELETE'])
def annuler_reservation(id):
    reservation = Reservation.query.get_or_404(id)

    db.session.delete(reservation)
    db.session.commit()

    return jsonify({"success": True, "message": "Réservation annulée avec succès."})



# création de clients pour faire une réservation
@main.route('/api/clients', methods=['POST'])
def ajouter_client():
    data = request.json
    nom = data.get('nom')
    email = data.get('email')

    if not nom or not email:
        return jsonify({"success": False, "message": "Veuillez fournir le nom et l'email du client."}), 400

    if Client.query.filter_by(email=email).first():
        return jsonify({"success": False, "message": "Cet email est déjà associé à un autre client."}), 400

    nouveau_client = Client(nom=nom, email=email)

    db.session.add(nouveau_client)
    db.session.commit()

    return jsonify({"success": True, "message": "Client ajouté avec succès."}), 201

