class TripConfirmer:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def confirm(self, trip_id) -> dict:
        try:
            self.__trip_repository.update_trip_status(trip_id)
            return {
                'body': None,
                'status_code': 204
            }
        except Exception as exception:
            return {
                'body': {'error': 'Bad Request', 'message': str(exception)},
                'status_code': 400
            }