from flask import jsonify, Blueprint, request

# Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder

# Repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

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

@trips_routes_bp.route('/trips/<trip_id>/invites', methods=['POST'])
def invite_to_trip(trip_id):
    connection = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(connection)
    emails_repository = EmailsToInviteRepository(connection)
    controller = ParticipantCreator(participants_repository, emails_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['POST'])
def create_activity(trip_id):
    connection = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(connection)
    controller = ActivityCreator(activities_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/participants', methods=['GET'])
def get_trip_participants(trip_id):
    connection = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(connection)
    controller = ParticipantFinder(participants_repository)

    response = controller.find_participants_from_trip(trip_id)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['GET'])
def get_trip_activities(trip_id):
    connection = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(connection)
    controller = ActivityFinder(activities_repository)

    response = controller.find_from_trip(trip_id)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/participants/<participant_id>/confirm', methods=['PATCH'])
def confirm_participant(participant_id):
    connection = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(connection)
    controller = ParticipantConfirmer(participants_repository)

    response = controller.confirm(participant_id)

    return jsonify(response['body']), response['status_code']