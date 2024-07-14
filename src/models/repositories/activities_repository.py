from sqlite3 import Connection

class ActivitiesRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def registry_activity(self, activity_infos: dict) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
                INSERT INTO activities (id, trip_id, title, occurs_at)
                VALUES (?, ?, ?, ?)
            """, (
                activity_infos['id'],
                activity_infos['trip_id'],
                activity_infos['title'],
                activity_infos['occurs_at']
            )
        )
        self.__connection.commit()
        cursor.close()

    def find_activities_from_trip(self, trip_id: str) -> list:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
                SELECT * FROM activities
                WHERE trip_id = ?
            """, (trip_id,)
        )
        activities = cursor.fetchall()
        cursor.close()
        return activities