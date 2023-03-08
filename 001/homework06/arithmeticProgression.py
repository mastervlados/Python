# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input("Input the first element = "))
difference_of_elements = int(input("Input difference = "))
dimension = int(input("Input dimension = "))

# init array/list
arithmetic_progression = list()

for i in range(dimension):
    if i == 0:
        # init [0] or first element that we know
        arithmetic_progression.append(first_element)
    else:
        new_element = arithmetic_progression[0] + i * difference_of_elements
        arithmetic_progression.append(new_element)

print(*arithmetic_progression)
