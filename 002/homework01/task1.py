def sort_list_imperative(numbers):
    # 10 9 8 7 6 5 4 3 2 1
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [x for x in numbers[1:] if x > pivot]
    right = [y for y in numbers[1:] if y <= pivot]
    return sort_list_imperative(left) + [pivot] + sort_list_imperative(right)

result = sort_list_imperative([3, 5, 2, 4, 10, 15, 7])
print(result)
result = sort_list_imperative([3, -5, 2, 4, -10, 15, -7])
print(result)