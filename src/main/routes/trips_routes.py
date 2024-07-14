from flask import jsonify, Blueprint, request

# Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

# Repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

# Connection
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint('trip_routes', __name__)

@trips_routes_bp.route('/trips', methods=['POST'])
def create_trip():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)
    emails_repository = EmailsToInviteRepository(connection)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>', methods=['GET'])
def find_trip(trip_id):
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(trip_id)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/confirm', methods=['PATCH'])
def confirm_trip(trip_id):
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(trip_id)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/links', methods=['POST'])
def create_trip_link(trip_id):
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/links', methods=['GET'])
def find_trip_links(trip_id):
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)
    controller = LinkFinder(links_repository)

    response = controller.find(trip_id)

    return jsonify(response['body']), response['status_code']