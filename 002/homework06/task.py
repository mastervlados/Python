sortedList = [22, 33, 44, 45, 46, 70, 71, 75, 80, 84, 85, 90, 91, 95, 100]

def getIndexOfElementCommon(list, element):
    index = -1
    iterations = 0
    for i, value in enumerate(list):
        iterations += 1
        if element == value:
            index = i
            print(f"Element {element} has index {index}")
            print(f"> Found solution from {iterations} iterations.")
            return index
    return index
    

getIndexOfElementCommon(sortedList, 95)
getIndexOfElementCommon(sortedList, 71)

def getIndexOfElementBinary(sortedList, element):
    index = -1
    steps = 0
    low = 0
    high = len(sortedList) - 1
    mid = 0

    while low <= high:
        steps += 1
        mid = (high + low) // 2

        # If element is greater, ignore left half
        if sortedList[mid] < element:
            low = mid + 1
        
        # If element is smaller, ignore right half
        elif sortedList[mid] > element:
            high = mid - 1
        
        # means element is present at mid
        else:
            print(f"Element {element} has index {mid}")
            print(f">> Found solution from {steps} steps.")
            return mid
    # If we reach here, then the element wasn't present
    return index

getIndexOfElementBinary(sortedList, 95)
getIndexOfElementBinary(sortedList, 71)
