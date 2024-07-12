from sqlite3 import Connection

class LinksRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def registry_link(self, link_infos: dict) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
                INSERT INTO links (id, trip_id, link, title) 
                VALUES (?, ?, ?, ?)
            ''', (
                link_infos['id'],
                link_infos['trip_id'],
                link_infos['link'],
                link_infos['title']
            )
        )
        self.connection.commit()
        cursor.close()

    def find_links_from_trip(self, trip_id: str) -> list:
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM links WHERE trip_id = ?', (trip_id,))
        links = cursor.fetchall()
        cursor.close()
        return links