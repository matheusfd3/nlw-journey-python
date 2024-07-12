from sqlite3 import Connection

class TripsRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def create_trip(self, trips_infos: dict) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
                INSERT INTO trips (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                trips_infos['id'],
                trips_infos['destination'],
                trips_infos['start_date'],
                trips_infos['end_date'],
                trips_infos['owner_name'],
                trips_infos['owner_email']
            )
        )
        self.__connection.commit()

    def find_trip_by_id(self, trip_id: str) -> tuple:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
                SELECT * FROM trips
                WHERE id = ?
            """, (trip_id,)
        )
        trip = cursor.fetchone()
        return trip
    
    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
                UPDATE trips
                SET status = 1
                WHERE id = ?
            """, (trip_id,)
        )
        self.__connection.commit()