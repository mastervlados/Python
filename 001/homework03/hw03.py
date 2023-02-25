import random

def fillListRandomNaturalNumbers(n):
    targetList = list()
    for i in range(1, n + 1): 
        targetList.append(random.randrange(1, 10 + 1)) # [1, 10) 1 - 9 | + 1
    print(*targetList)
    return targetList

def getNumber():
    flag = True
    while flag:
        naturalNumber = int(input("Input number from 1 to 10: X = "))
        if naturalNumber >= 1 and naturalNumber <= 10:
            flag = False # end loop
        else:
            print(f"> {naturalNumber} isn't correct number!")
    return naturalNumber
# ********************
# **** Задача 16: ****
# ********************
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
dimension = int(input("Input list size: N = "))
listWithNaturalNumbers = fillListRandomNaturalNumbers(dimension)

times = 0
userNumber = getNumber()
for i in listWithNaturalNumbers:
    if i == userNumber:
        times += 1

print("-> {} times".format(times))

# ********************
# **** Задача 18: ****
# ********************
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
print("\n")
dimension = int(input("Input list size: N = "))
listWithNaturalNumbers = fillListRandomNaturalNumbers(dimension)

minValue = listWithNaturalNumbers[0]
maxValue = getNumber() # target number

for i in listWithNaturalNumbers:
    if maxValue > i:
        minValue = i
    elif minValue + 1 == maxValue:
        break

print("-> {} is near to {}".format(minValue, maxValue))

# ********************
# **** Задача 20: ****
# ********************
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12
print("\n")
# **😈*****************************************************************
# **** This task contains the business value for my Telegram bots! ****
# *****************************************************************👿**
import re
botName = "President Rias"
# В случае с английским алфавитом очки распределяются так:
#   A, E, I, O, U, L, N, S, T, R – 1 очко; 
#   D, G – 2 очка; 
#   B, C, M, P – 3 очка; 
#   F, H, V, W, Y – 4 очка; 
#   K – 5 очков; 
#   J, X – 8 очков; 
#   Q, Z – 10 очков. 
scrabbleEn = {
    'A' : 1,
    'E' : 1,
    'I' : 1,
    'O' : 1,
    'U' : 1,
    'L' : 1,
    'N' : 1,
    'S' : 1,
    'T' : 1,
    'R' : 1,
    'D' : 2,
    'G' : 2,
    'B' : 3,
    'C' : 3,
    'M' : 3,
    'P' : 3,
    'F' : 4,
    'H' : 4,
    'V' : 4,
    'W' : 4,
    'Y' : 4,
    'K' : 5,
    'J' : 8,
    'X' : 8,
    'Q' : 10,
    'Z' : 10,
}
# А русские буквы оцениваются так: 
#   А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
#   Д, К, Л, М, П, У – 2 очка; 
#   Б, Г, Ё, Ь, Я – 3 очка; 
#   Й, Ы – 4 очка; 
#   Ж, З, Х, Ц, Ч – 5 очков; 
#   Ш, Э, Ю – 8 очков; 
#   Ф, Щ, Ъ – 10 очков. 
scrabbleRu = {
    'А' : 1,
    'В' : 1,
    'Е' : 1,
    'И' : 1,
    'Н' : 1,
    'О' : 1,
    'Р' : 1,
    'С' : 1,
    'Т' : 1,
    'Д' : 2,
    'К' : 2,
    'Л' : 2,
    'М' : 2,
    'П' : 2,
    'У' : 2,
    'Б' : 3,
    'Г' : 3,
    'Ё' : 3,
    'Ь' : 3,
    'Я' : 3,
    'Й' : 4,
    'Ы' : 4,
    'Ж' : 5,
    'З' : 5,
    'Х' : 5,
    'Ц' : 5,
    'Ч' : 5,
    'Ш' : 8,
    'Э' : 8,
    'Ю' : 8,
    'Ф' : 10,
    'Щ' : 10,
    'Ъ' : 10,
}

def getWord():
    flag = True
    patternEn = "^\S[a-zA-Z]+$" # case sensitive
    patternRu = "^\S[а-яА-Я]+$" # \S fixes spaces
    language = "en"
    while flag:
        word = str(input(f"{botName} > Input one word: "))
        if bool(re.search(patternEn, word)):
            flag = False
        elif bool(re.search(patternRu, word)):
            language = "ru"
            flag = False
        else:
            print(f"{botName} > »{word}« isn't correct!")
    return (word, language) # OK!

userInputWord = getWord() # tuple (word, language)

def getHowMuchWordCosts(word, lang):
    
    def getPrice(word, dictionary): # it will work with necessary data Ru/En
        price = 0
        for i in word:
            price += dictionary[i.upper()] # make up each char
        return price
    
    itCosts = 0
    if lang == "en":
        itCosts = getPrice(word, scrabbleEn)
    elif lang == "ru":
        itCosts = getPrice(word, scrabbleRu)
    print("Scrabble > »{}« стоит {} очков!".format(word, itCosts))

getHowMuchWordCosts(userInputWord[0], userInputWord[1])
