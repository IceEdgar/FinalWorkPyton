from datetime import datetime
import csv
import os
import shutil

class Note_pad:
    number_line = None 

def add_note():
        if os.path.isfile("file.csv") == False: 
            headerlist = ({"name_note": [], "text_note": [], "date_time": []})
            with open("file.csv", "w", newline="", encoding="utf-8") as file_note:
                d_writer = csv.DictWriter(file_note, delimiter=";",fieldnames=headerlist)
                d_writer.writeheader()
        print('Введите имя новой заметки:')
        new_name_note = input()
        print('Введите текст заметки:')
        text_note = input()
        date_current = str(datetime.now().strftime("%d.%m.%Y"))
        with open("file.csv", "a", newline="", encoding="utf-8") as note:
            writer = csv.writer(note, delimiter=";")
            writer.writerow([new_name_note, text_note, date_current])
            print("Заметка успешно создана!")

def list_note():
        print('Список заметок:')
        with open("file.csv", encoding="utf-8") as note_list:
            reader = csv.DictReader(note_list, delimiter=";")
            for row in reader:
                print(row["name_note"])
        
                    
def show_note():
        logic = True
        print("Введите имя заметки:")
        name = input()
        number_line = None 
        with open("file.csv", encoding="utf-8") as line:
            reader = csv.DictReader(line, delimiter=";")
            for i, row in enumerate(reader):
                if row["name_note"] == name:
                    number_line = i
                    with open("file.csv", encoding="utf-8") as csv_file:
                        csv_reader = csv.reader(csv_file)
                        rows = list(csv_reader)
                        print(rows[number_line + 1])
                        logic = False
        if logic == True:
            print("такой заметки нет!!!")

def show_date():
    logic = True
    date = input('Введите дату в формате dd.mm.yyyy: ')
    number_line = None 
    with open("file.csv", encoding="utf-8") as line:
        reader = csv.DictReader(line, delimiter=";")
        for i, row in enumerate(reader):
            if row["date_time"] == date:
                number_line = i
                with open("file.csv", encoding="utf-8") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    rows = list(csv_reader)
                    print(rows[number_line + 1])
                    logic = False
        if logic == True:
            print("Нет ни одной заметки с такой датой")

def edit_note():
        logic = True
        print("Введите имя заметки:")
        name = input()
        number_line = None 
        with open("file.csv", encoding="utf-8") as line:
            reader = csv.DictReader(line, delimiter=";")
            for i, row in enumerate(reader):
                if row["name_note"] == name:
                    number_line = i
                    with open("file.csv", encoding="utf-8", newline='') as source, open("new_file.csv", "w", encoding="utf-8", newline='') as dest:
                        reader = csv.reader(source, delimiter=';')
                        writer = csv.writer(dest,delimiter=';')
                        for line,rows in enumerate(reader):
                            if line != number_line + 1:
                                writer.writerow(rows)
                            if line == number_line + 1:
                                date_current = str(datetime.now().strftime("%d.%m.%Y"))
                                print("Введите новый текст заметки:")
                                new_text = input()
                                writer.writerow([row["name_note"], new_text, date_current])
                    shutil.copy2(r"new_file.csv", r"file.csv")
                    os.remove('new_file.csv')
                    print("Заметка изменена")
                    logic = False
        if logic == True:
            print("такой заметки нет") 
        

def del_note():
        logic = True 
        print("Введите имя заметки:")
        name = input()
        number_line = None 
        with open("file.csv", encoding="utf-8") as line:
            reader = csv.DictReader(line, delimiter=";")
            for i, row in enumerate(reader):
                if row["name_note"] == name:
                    number_line = i
                    with open("file.csv", newline='') as source, open("new_file.csv", "w", newline='') as dest:
                        reader = csv.reader(source, delimiter=';')
                        writer = csv.writer(dest,delimiter=';')
                        for line,row in enumerate(reader):
                            if line != number_line + 1:
                                writer.writerow(row)
                    shutil.copy2(r"new_file.csv", r"file.csv")
                    os.remove('new_file.csv')
                    print("Заметка успешно удалена")
                    logic = False
        if logic == True:
            print("такой заметки нет")      
        

            