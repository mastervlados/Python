def merge_sort(arr):
    arrLength = len(arr)
    if arrLength <= 1: 
        return arr
    
    middle = arrLength // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)
    
def merge(left, right):
    sortedArr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            sortedArr.append(left[0])
            left = left[1:]
        else:
            sortedArr.append(right[0])
            right = right[1:]
    if len(left) > 0:
        sortedArr += left
    if len(right) > 0:
        sortedArr += right
    return sortedArr

my_array = [64, 34, 25, 12, 22, 11, 90] # Создание неотсортированного массива.
new_array = merge_sort(my_array) # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", new_array) # Вывод отсортированного массива.

# def merge_sort(arr):
#     if len(arr) > 1: # Проверка, что длина массива больше 1 (иначе сортировка не нужна).
        
#         mid = len(arr) // 2 # Вычисление середины массива.
#         left_half = arr[:mid] # Создание левой половины массива.
#         right_half = arr[mid:] # Создание правой половины массива.

#         # Рекурсивный вызов merge_sort для левой и правой половин массива.
#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0  # Инициализация индексов для объединения двух половин.

#         # Объединение левой и правой половин в один отсортированный массив.
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
#                 arr[k] = left_half[i]  # Если элемент из левой меньше, помещаем его в исходный массив.
#                 i += 1
#             else:
#                 arr[k] = right_half[j]  # Если элемент из правой меньше, помещаем его в исходный массив.
#                 j += 1
#             k += 1

#         # Добавление оставшихся элементов из левой и правой половин (если такие есть).
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

