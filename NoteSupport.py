from datetime import datetime
from NoteJson import NoteJson


class NoteSupport(NoteJson):
    def __init__(self, path):
        super().__init__(path)

    def get_free_id(self) -> int:
        data = self.read_json()
        if len(data['id']) == 0:
            return 1
        else:
            id = data['id']
            return max(id) + 1

    def get_index_by_id(self, id: int) -> int:
        data = self.read_json()
        list_id = data['id']
        index = list_id.index(id)
        return index

    def datetime_serializer(self, time):
        if isinstance(time, datetime):
            return time.isoformat()

    def get_datetime(self, iso_string: str):
        datetime_obj = datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%S.%f')
        return datetime_obj.year, datetime_obj.month, datetime_obj.day, datetime_obj.hour, datetime_obj.minute
