import pytest
import uuid
from datetime import datetime, timedelta
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='This test is used to create a trip in the database')
def test_create_trip():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trips_infos = {
        'id': trip_id,
        'destination': 'São Paulo',
        'start_date': datetime.strptime("02-01-2024", "%d-%m-%Y"),
        'end_date': datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        'owner_name': 'Lucas',
        'owner_email': 'lucas@email.com'
    }

    trips_repository.create_trip(trips_infos)

@pytest.mark.skip(reason='This test is used to find a trip by id in the database')
def test_find_trip_by_id():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)

@pytest.mark.skip(reason='This test is used to update a trip status in the database')
def test_update_trip_status():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trips_repository.update_trip_status(trip_id)