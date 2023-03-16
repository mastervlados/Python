# Задача 38:
# CRUD - Create Read Update Delete 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

# Задача 39:
# 1. импорт/экспорт данных в .txt
# 2. Фамилия, Имя, Отчество, Номер телефона - пробелом

# Требования:
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные (data.txt)
# 3. Пользователь может ввести одну из характеристик для поиска записи
# 4. Использование функций. Программа не должна быть линейной

import os
import modules.user as user
import modules.ui as ui

def run(data):
    # Load data from data.txt
    data
    # Show user interface
    ui.show_menu()
    flag = True
    while flag:
        action = user.get_action_number()
        match action:
            case 1: # show
                ui.show_all_data(data)
                message = "Would you like to continue?"
                if user.get_answer_to(message):
                    ui.show_menu()
                else:
                    break
            case 2: # find
                ui.find_data(data)
                message = "Would you like to go back menu?"
                if user.get_answer_to(message):
                    ui.show_menu()
                else:
                    break
            case 3: # add
                data = ui.add_data(data)
                ui.show_menu()
            case 4: # save
                ui.save_data(data)
                message = "Would you like to continue?"
                if user.get_answer_to(message):
                    ui.show_menu()
                else:
                    break
            case 5: # edit
                data = ui.edit_data(data)
                ui.show_menu()
            case 6: # delete
                data = ui.delete_contact(data)
                ui.show_menu()
            case 7: # import
                break
            case 8: # export
                break
            case _: # exit, suggest 0
                message = "If you have unsaved data it'll be lost.. Close the program?"
                if user.get_answer_to(message):
                    flag = False
                else:
                    ui.show_menu()
                    
# check for file <data.txt> *if create new
if os.path.isfile('data.txt') != True:
    open('data.txt', 'a', encoding='utf-8').close()    


data = open('data.txt', 'r', encoding='utf-8')
phone_book = set()
for line in data:
    # keep only uniq lines
    phone_book.add(line.replace('\n', ''))
data.close()


contacts_list = list()
for i in phone_book:
    i = i.split(' ')
    # [0] = surname
    # [1] = name
    # [2] = middle_name
    # [3] = phone_number
    contacts_list.append({
    'surname':i[0],
    'name':i[1],
    'middle_name':i[2],
    'phone_number':i[3],
    })

# *********************
# **** RUN PROGRAM ****
# *********************
run(contacts_list)