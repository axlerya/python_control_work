from Note import Note
from NoteView import NoteView


class NoteMain:
    path = 'data.json'
    view = NoteView(path)
    note = Note(path)

    def add(self):
        title, body = self.input_for_note()
        self.note.add_note(title, body)

    def edit(self, id: int):
        title, body = self.input_for_note()
        self.note.edit_note(id, title, body)

    def delete(self, id: int):
        self.note.delete_note(id)

    def show(self, id=None):
        if id == None:
            self.view.print_console_all()
        else:
            self.view.print_console_by_id(id)

    def input_for_note(self):
        title = input('Введите заголовок')
        body = input('Введите заметку')
        return title, body


note = NoteMain()

while True:
    print('''
          =============================
          add - добавить заметку
          edit - редактировать заметку
          delete - удалить заметку
          show - показать заметку(и)
          exit - выход
          =============================
          ''')
    command = input("Введите команду")

    match command:
        
        case 'add':
            note.add()

        case 'edit':
            try:
                id = int(input('Введите ID заметки для редактирования'))
            except:
                print("Некорректный ввод: ID")
            try:
                note.edit(id)
            except:
                print("Заметки с таким ID не существует")

        case 'delete':
            try:
                id = int(input('Введите ID заметки для удаления'))
            except:
                print("Некорректный ввод: ID")
            try:
                note.delete(id)
            except:
                print("Заметки с таким ID не существует")

        case 'show':
            id = input(
                'Введите ID заметки для просмотра. Для просмотра всех заметок оставьте поле ввода пустым')
            if id == '':
                note.show()
            else:
                try:
                    id = int(id)
                    note.show(id)
                except:
                    print("Некорректный ввод: ID")

        case 'exit':
            break

        case _:
            print("Некорректный ввод команды")
