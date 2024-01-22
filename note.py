from random import *
import json

note = {}

def new():
    name = input('Введите название заметки ')
    list = input('Введите текст заметки ')
    print('Незабудьте сохранить введенную заметку')

    note[name] = {name : list}
    

def save():
    with open('note.json', 'a') as file:
        json.dump(note, file,indent=4, ensure_ascii=False)
    print('Заметка успешно добавлена в блокнот')

def edit():
    name = input('Введите название сохраненной заметки ')
    list = input('Введите текст заметки ')
    print('Незабудьте сохранить введенную заметку')

    note[name] = {name : list}




while True:
    command = input('Введите команду ')
    if command == 'start':                                    # Начало работы 
        print('Добро пожаловать в ваш блокнот')
    if command == 'stop': 
        print('Надеюсь Вам понравилось.')                     # Конец работы
        break
    elif command == 'all':                                    # Показать список заметок
        print(note.keys())
    elif command == 'new':                                    # Добавить новую заметку, редактировать заметку 
        new()
    elif command == 'edit':                                   # Редактировать текс созданой заметки
        edit()
    elif command == 'save':                                   # Сохранить заметку
        save()
    elif command == 'show':                                   # Показать данные контакта
        name_1 = input('Введите название заметки ')
        print(note[name_1])
    elif command == 'del':                                    # Удаление контакта
        name_2 = input('Введите название заметки ')
        del(note[name_2])
        print('Заметка успешно удалена из блокнота')
    elif command == 'load':                                     #Загрузить файл контактов
        with open('note.json') as file:
            note=json.load(file)

            