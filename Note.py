from datetime import datetime
from NoteSupport import NoteSupport


class Note(NoteSupport):
    def __init__(self, path):
        super().__init__(path)

    def add_note(self, title: str, body: str):

        id_list, title_list, body_list, date_list = self.parse_json()

        id_list.append(self.get_free_id())
        title_list.append(title)
        body_list.append(body)
        date_list.append(self.datetime_serializer(datetime.now()))

        self.write_json(id_list, title_list, body_list, date_list)

    def edit_note(self, id: int, title: str, body: str):

        id_list, title_list, body_list, date_list = self.parse_json()
        index = self.get_index_by_id(id)

        title_list[index] = title
        body_list[index] = body
        date_list[index] = self.datetime_serializer(datetime.now())

        self.write_json(id_list, title_list, body_list, date_list)

    def delete_note(self, id: int):

        id_list, title_list, body_list, date_list = self.parse_json()
        index = self.get_index_by_id(id)

        id_list.pop(index)
        title_list.pop(index)
        body_list.pop(index)
        date_list.pop(index)

        self.write_json(id_list, title_list, body_list, date_list)



