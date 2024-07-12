from sqlite3 import Connection

class EmailsToInviteRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def registry_email(self, email_infos: dict) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
                INSERT INTO emails_to_invite (id, trip_id, email)
                VALUES (?, ?, ?)
            """, (
                email_infos['id'],
                email_infos['trip_id'],
                email_infos['email']
            )
        )
        self.__connection.commit()

    def find_emails_from_trip(self, trip_id: str) -> list:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
                SELECT * FROM emails_to_invite
                WHERE trip_id = ?
            """, (trip_id,)
        )
        emails = cursor.fetchall()
        return emails