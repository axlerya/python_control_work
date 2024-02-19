from NoteSupport import NoteSupport


class NoteView(NoteSupport):
    def __init__(self, path):
        super().__init__(path)
        
    def print_console_all(self):
        id_list, title_list, body_list, date_list = self.parse_json()
        
        for i in id_list:
            self.print_console_by_id(i)
            
            
    def print_console_by_id(self, id: int):
        id_list, title_list, body_list, date_list = self.parse_json()
        i = self.get_index_by_id(id)
        
        year, month, day, hour, minute = self.get_datetime(date_list[i])
        
        print(f"=====================================\n              Заметка №{id_list[i]} ")
        print(f"ID: {id_list[i]}\nЗаголовок: {title_list[i]}\nТело: {body_list[i]}")
        print(f"Дата: {year}:{month}:{day} Время: {hour}:{minute}")
        
    
        
        
        

