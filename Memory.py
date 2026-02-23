from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup,  QListWidget, QTextEdit, QLineEdit, QInputDialog
import json
app = QApplication([])

notes = []
# notes = {
#     'Добро пожаловать!' : {
#         'текст': 'Это самое удобное приложение для заметок!',
#         'теги': ['правила', 'инструкция']
#     }
# }
# with open('notes_data.json', 'w') as file:
#     json.dump(notes, file)



Win = QWidget()
Win.setWindowTitle('Умные заметки')
Win.resize(900,600)

list_note = QListWidget()
list_note_name = QLabel('Список заметок:')

buttom_n_create = QPushButton('Создать заметку.')
buttom_n_delite = QPushButton('Удалить заметку.')
buttom_n_save = QPushButton('Сохранить заметку.')

field_tags = QLineEdit()
field_tags.setPlaceholderText('Введите тег...')
field_tags_text = QTextEdit()
buttom_t_add = QPushButton('Добавить тег к заметке.')
buttom_t_delite = QPushButton('Снять тег с заметки.')
buttom_t_search = QPushButton('Искать заметку по тегу')
list_tags = QListWidget()
list_tags_name = QLabel('Список тегов:')

layout_note = QHBoxLayout()
layout_col1 = QVBoxLayout()
layout_col1.addWidget(field_tags_text)

layout_col2 = QVBoxLayout()
layout_col2.addWidget(list_note_name)
layout_col2.addWidget(list_note)
layout_row1 = QHBoxLayout()
layout_row1.addWidget(buttom_n_create)
layout_row1.addWidget(buttom_n_delite)
layout_row2 = QHBoxLayout()
layout_row2.addWidget(buttom_n_save)
layout_col2.addLayout(layout_row1)
layout_col2.addLayout(layout_row2)

layout_col2.addWidget(list_tags_name)
layout_col2.addWidget(list_tags)
layout_col2.addWidget(field_tags)
layout_row3 = QHBoxLayout()
layout_row3.addWidget(buttom_t_add)
layout_row3.addWidget(buttom_t_delite)
layout_row4 = QHBoxLayout()
layout_row4.addWidget(buttom_t_search)

layout_col2.addLayout(layout_row3)
layout_col2.addLayout(layout_row4)

layout_note.addLayout(layout_col1, stretch=2)
layout_note.addLayout(layout_col2, stretch=1)
Win.setLayout(layout_note)

def show_note():
    key =list_note.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_tags_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])
# def show_note():
#     name = list_note.selectedItems()[0].text()
#     field_tags_text.setText(notes[name]['текст'])
#     list_tags.clear()
#     list_tags.addItems(notes[name]['теги'])
# list_note.itemClicked.connect(show_note)

Win.show()

# with open('notes_data.json', 'r') as file:
#     notes = json.load(file)
# list_note.addItems(notes)

def add_note():
    note_name, ok = QInputDialog.getText(
        Win, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_note.addItem(note[0])
        list_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+'\n')





# def add_note():
#     list_note_name, ok = QInputDialog.getText(
#         Win, 'Добавить заметку', 'Название заметки:')
#     if ok and list_note_name != '':
#         notes[list_note_name] = {"текст" : "", "теги" : []}
#         list_note.addItem(list_note_name)
#         list_tags.addItems(notes[list_note_name]["теги"])
#         print(notes)

def save_note():
    if list_note.selectedItems():
        key =list_note.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_tags_text.toPlainText()
                with open(str(index)+'.txt', 'w') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+'')
                    file.write('\n')
            index +=1
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index)+".txt", "w") as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index += 1
        print(notes)
    else:
        print("Заметка для сохранения не выбрана!")




# def save_note():
#     if list_note.selectedItems():
#         key =list_note.selectedItems()[0].text()
#         notes[key]['текст'] = field_tags_text.toPlainText()
#         with open('notes_data.json', 'w') as file:
#             json.dump(notes, file, sort_keys=True, ensure_ascii=False) 
#         print(notes)
#     else:
#         print('Заметка для сохранения не выбрана!')

# def del_note():
#     if list_note.selectedItems():
#         key = list_note.selectedItems()[0].text()
#         del notes[key]
#         list_note.clear()
#         list_tags.clear()
#         field_tags_text.clear()
#         list_note.addItems(notes)
#         with open('notes_data.json', 'w') as file:
#             json.dump(notes, file, sort_keys=True, ensure_ascii=False)
#         print(notes)
#     else:
#         print('Заметка для удаления не выбрана!')



# def del_tag():
#     if list_tags.selectedItems():
#         key = list_note.selectedItems()[0].text()
#         tag = list_tags.selectedItems()[0].text()
#         notes[key]['теги'].remove(tag)
#         list_tags.clear()
#         list_tags.addItems(notes[key]['теги'])
#         with open('notes_data.json', 'w') as file:
#             json.dump(notes, file, sort_keys=True, ensure_ascii=False)
#         print(notes)
#     else:
#         print('Тег для удаления не выбрана!')

# def add_tag():
#     if list_note.selectedItems():
#         key = list_note.selectedItems()[0].text()
#         tag = field_tags.text()
#         if not tag in notes[key]['теги'] != '':
#             notes[key]['теги'].append(tag)
#             list_tags.addItem(tag)
#             field_tags.clear()
#         with open('notes_data.json', 'w') as file:
#             json.dump(notes, file, sort_keys=True, ensure_ascii=False) 
#         print(notes)
#     else:
#         print('Заметка для добавления тега не выбрана!')


# def search_tags():
#     tag = field_tags.text()
#     if buttom_t_search.text() == 'Искать заметку по тегу' and tag:
#         # print(tag)
#         notes_filtered = {}
#         for note in notes:
#             if tag in notes[note]['теги']:
#                 notes_filtered[note] = notes[note]
#         buttom_t_search.setText('Сбросить поиск')
#         list_note.clear()
#         list_tags.clear()
#         list_note.addItems(notes_filtered)
#     elif buttom_t_search.text() == 'Сбросить поиск':
#         list_note.clear()
#         list_tags.clear()
#         field_tags.clear()
#         list_note.addItems(notes)
#         buttom_t_search.setText('Искать заметку по тегу')
#     else:
#         pass
# name = 0
# note = []
# while True:
#     filename = str(name)+'.txt'
#     try:
#         with open(filename,'r')as file:
#             for line in file:
#                 line = line.replace('\n', '')
#                 note.append(line)
#         tags = note[2].split(' ')
#         note[2] = tags
#         notes.append(note)
#         note = []
#         name +=1
#     except IOError:
#         break
# while True:
#     filename = str(name)+".txt"
#     try:
#         with open(filename, "r") as file:
#             for line in file:
#                 line = line.replace('\n', '')
#                 note.append(line)
#         tags = note[2].split(' ')
#         note[2] = tags
        
#         notes.append(note)
#         note = []
#         name += 1


#     except IOError:
#         break

print(notes)
for note in notes:
    list_note.addItem(note[0])

# list_note.itemClicked.connect(show_note)
# buttom_n_create.clicked.connect(add_note)
# buttom_n_save.clicked.connect(save_note)
# buttom_n_delite.clicked.connect(del_note)
# buttom_t_delite.clicked.connect(del_tag)
# buttom_t_add.clicked.connect(add_tag)
# buttom_t_search.clicked.connect(search_tags)
app.exec_()
#затем запрограммируй демо-версию функционала
