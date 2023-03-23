PROGRAM_NAME = "Phone Book"
MENU_TITLE = "Menu"
SHOW_TITLE = "User List"
ADD_TITLE = "Adding Mode"
SAVE_TITLE = "Saving.."
FIND_TITLE = "Finding.."
EDIT_TITLE = "Editing Mode"
DELETE_TITLE = "Deleting.."

breadcrumbs = f"{PROGRAM_NAME} > {MENU_TITLE}"

import os
import modules.user as user

def clear_console():
    os.system('CLS')

def show_menu():
    clear_console()
    print(breadcrumbs)
    print("+------------+-------------+-------------+")
    print("|  1 - Show  | 4 - Save    | 7 - Import  |")
    print("|  2 - Find  | 5 - Edit    | 8 - Export  |")
    print("|  3 - Add   | 6 - Delete  | 0 - Exit    |")
    print("+------------+-------------+-------------+")

def show_data(data):
    count = 0
    for i in data: 
        count += 1
        print(*(
            i['surname'],
            i['name'],
            i['middle_name'],
            i['phone_number'],
        ))
    return count

def find_contact_by_phone_number(data, criteria):
        index = -1
        for i, val in enumerate(data):
            if val['phone_number'] == criteria:
                index = i
                break
        return index

def contact_details(data, index):
    print(f"1 | Surename = {data[index]['surname']}")
    print(f"2 | Name = {data[index]['name']}")
    print(f"3 | Middle Name = {data[index]['middle_name']}")
    print(f"4 | Phone Number = {data[index]['phone_number']}")
    print(f"0 | Exit")
 
def show_all_data(data):
    clear_console()
    print(breadcrumbs, f"> {SHOW_TITLE}")
    count = show_data(data)
    if count == 0:
        print("... no contacts here yet")
    else:
        print(f"... contains {count} users")

def find_data(data):
    clear_console()
    print(breadcrumbs, f"> {FIND_TITLE}")
    term = input("Type «Name» or «Surename» to find contacts > ").lower()
    new_data = list(filter(lambda item: term in item['name'].lower() or term in item['surname'].lower(), data))
    count = show_data(new_data)
    if count == 0:
        print("... no contacts found")
    else:
        print(f"... exist {count} users")

def add_data(data):
    clear_console()
    print(breadcrumbs, f"> {ADD_TITLE}")
    flag = True
    while flag:
        surname = input("*New Surname > ") 
        name = input("*New Name > ") 
        middle_name = input("*New Middle Name > ") 
        phone_number = user.get_phone_number("*New Phone Number")
        new_data = [*data, {
            'surname': surname, 
            'name': name, 
            'middle_name': middle_name, 
            'phone_number': phone_number, 
        }]
        print(surname, name, middle_name, phone_number, "was added!")
        # Suggest to add next
        message = "Would you like add another one?"
        if user.get_answer_to(message):
            continue
        else:
            flag = False
    return new_data

def save_data(program_data):
    clear_console()
    print(breadcrumbs, f"> {SAVE_TITLE}")
    data = open('data.txt', 'w', encoding='utf-8')
    for i in program_data:
        data.write("{} {} {} {}\n".format(i['surname'], i['name'], i['middle_name'], i['phone_number']))
    data.close()
    print("\nThe list was saved successfully in 'data.txt'")

def edit_data(data):
    clear_console()
    print(breadcrumbs, f"> {EDIT_TITLE}")
    flag = True
    while flag:
        criteria = user.get_phone_number("*Type «Phone Number» of exist user\nyou want to edit")
        index = find_contact_by_phone_number(data, criteria)
        if index == -1:
            print("\nThat number doesn't exist..")
        else:
            contact_details(data, index)
            print("\nYou need to type a number to edit field")
            while True:
                action = user.get_action_number()
                match action:
                    case 1: # surename
                        data[index]['surname'] = input("*New Surname > ")
                        print("Contact was updated!")
                    case 2: # name
                        data[index]['name'] = input("*New Name > ")
                        print("Contact was updated!")
                    case 3: # middle_name
                        data[index]['middle_name'] = input("*New Middle Name > ")
                        print("Contact was updated!")
                    case 4: # phone_number
                        data[index]['phone_number'] = user.get_phone_number("*New Phone Number")
                        print("Contact was updated!")
                    case _: # complete
                        break
        # Contunue editing?
        message = "Would you like to continue editing contacts?"
        if user.get_answer_to(message):
            continue
        else:
            flag = False    
    return data

def delete_contact(data):
    clear_console()
    print(breadcrumbs, f"> {DELETE_TITLE}")
    flag = True
    while flag:
        criteria = user.get_phone_number("*Type «Phone Number» of exist user\nyou want to delete")
        index = find_contact_by_phone_number(data, criteria)
        if index == -1:
            print("\nThat number doesn't exist..")
        else:
            data.pop(index) # delete the element
            print("\nContact was deleted!")
        # Contunue editing?
        message = "Would you like to continue deleting contacts?"
        if user.get_answer_to(message):
            continue
        else:
            flag = False  
    return data
