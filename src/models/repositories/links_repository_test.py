import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()

link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='This test is used to registry a link in the database')
def test_registry_link():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    link_infos = {
        'id': link_id,
        'trip_id': trip_id,
        'link': 'https://www.google.com',
        'title': 'Google'
    }

    links_repository.registry_link(link_infos)

@pytest.mark.skip(reason='This test is used to find links from a trip in the database')
def test_find_links_from_trip():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    links = links_repository.find_links_from_trip(trip_id)
    
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)