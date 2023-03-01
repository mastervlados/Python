# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def get_custom_list(char):
    dimension = int(input(f"Input list size: {char.upper()} = "))
    custom_list = list() # will append new values
    for i in range(dimension):
            user_value = int(input(f"Input List[{i}] = "))
            custom_list.append(user_value)
    return custom_list


first_list = get_custom_list('n')
second_list = get_custom_list('m')

# first_list = [2, 5, 4, 10, 15, 2, 5, 6, 4, 10]
# second_list = [11, 52, 10, 4, 2, 5, 6, 8, 8, 9, 1]

print("Print arrays:")
print("List 1: ", *first_list)
print()
print("List 2: ", *second_list)
print()

# delete repeat values and merge lists
# list to set (only uniq values)
uniq_set = set(first_list + second_list)
uniq_list = list(uniq_set) # set back to list (use indexes)

# small to large all numbers (sort)
# bubble sort
length = len(uniq_list)
for i in range(length):
    for j in range(length - i - 1):
        if uniq_list[j] > uniq_list[j + 1]:
            uniq_list[j], uniq_list[j + 1] = uniq_list[j + 1], uniq_list[j]
print(uniq_list)