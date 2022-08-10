from peewee import *

db = PostgresqlDatabase('notes', user='denny', password='123',
                        host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Notes(BaseModel):
    id = AutoField()
    title = CharField()
    content = CharField()

def view():
    for item in Notes.select():
        print(f'{[item.id, item.title, item.content]}')

def add():
    title = input("Title of note? ")
    content = input("Contents of note? ")
    new_note = Notes(title=f'{title}', content=f'{content}')
    new_note.save()
    print('Note has been added\n')

def find_by_id():
    try:
        note_id = input('Note Id? ')
        result = Notes.get(Notes.id == f'{note_id}')
        print(f'Note #{result.id}, Title: {result.title}, Content: {result.content}')
    except:
        print('Note not found')

def note():
    try:
        query = input('Search notes by title: ')
        result = Notes.get(Notes.title.contains(query))
        print([result.id, result.title, result.content])
    except:
        print(f'There are no notes that contains title "{query}"')

while True:
    print("Welcome to Super Notes!")
    print("1. Create Note\n"
          "2. View All Notes\n"
          "3. Find Note By Number\n"
          "4. Search for Note By Title\n"
          "5. Exit")

    option = input('Pick an option: ')
    if option == '1':
        add()
    elif option == '2':
        view()
    elif option == '3':
        find_by_id()
    elif option == '4':
        note()
    elif option == '5':
        print("Goodbye!")
        break