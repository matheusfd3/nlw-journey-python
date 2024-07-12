import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='This test is used to registry an email in the database')
def test_registry_email():
    connection = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(connection)

    email_trips_infos = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'email': 'olaMundo@email.com'
    }

    emails_to_invite_repository.registry_email(email_trips_infos)

@pytest.mark.skip(reason='This test is used to find emails from a trip in the database')
def test_find_emails_from_trip():
    connection = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(connection)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)