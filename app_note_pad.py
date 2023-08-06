import note_pad_function


while True:
    p = input("Введите цыфру из МЕНЮ:\n\
    1 - Создать новую заметку\n\
    2 - Просмотреть список всех заметок\n\
    3 - Посмотреть заметку\n\
    4 - Изменить заметку\n\
    5 - Найти заметку по дате\n\
    6 - Удалить заметку\n\
    Введите номер действия из Меню: ")
    if  p == '1': note_pad_function.add_note() 
    elif p == '2': note_pad_function.list_note()
    elif p == '3': note_pad_function.show_note()
    elif p == '4': note_pad_function.edit_note()
    elif p == '5': note_pad_function.show_date()
    elif p == '6': note_pad_function.del_note()
    else: print('Некорректный ввод')
