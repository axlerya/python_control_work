import json

class NoteJson:
    def __init__(self, path):
        self.path = path

    def read_json(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def write_json(self, id_list, title_list, body_list, date_list):
        data = {
            "id": id_list,
            "title": title_list,
            "body": body_list,
            "date": date_list
        }
        
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        
    def parse_json(self):
        data = self.read_json()
        id_list = data['id']
        title_list = data['title']
        body_list = data['body']
        date_list = data['date']
        
        return id_list, title_list, body_list, date_list
    
    
