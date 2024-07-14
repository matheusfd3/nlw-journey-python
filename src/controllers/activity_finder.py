class ActivityFinder:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def find_from_trip(self, trip_id: str) -> dict:
        try:
            activities = self.__activity_repository.find_activities_from_trip(trip_id)

            activities_infos = []
            for activity in activities:
                activities_infos.append({
                    'id': activity[0],
                    'title': activity[2],
                    'occurs_at': activity[3],
                })

            return {
                'body': {
                    'activities': activities_infos
                },
                'status_code': 200
            }
        except Exception as exception:
            return {
                'body': {
                    'error': 'Bad Request',
                    'message': str(exception)
                },
                'status_code': 400
            }
        