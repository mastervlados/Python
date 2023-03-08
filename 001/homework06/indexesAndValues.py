# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_number = int(input("Input number min = "))
max_number = int(input("Input number max = "))

print("in: ", *list_1, "\n")

count = 0

for i, value in enumerate(list_1):
    if min_number <= value <= max_number:
        print(f"index: {i}  value: {value}")
        count += 1

if count == 0:
    print("\n> 0 results found.")
else:
    print(f"\n> {count} results.")