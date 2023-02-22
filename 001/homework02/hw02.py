# ********************
# **** Задача 10: ****
# ********************
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
coins = int(input("Сколько монет лежит на столе? = "))
theCoinsAreTails = 0
theCoinsAreEagles = 0
while coins > 0:
    nextCoinIs = int(input(f"Монет осталось:{coins}\nВведите 1 (елсли орел) 0 (решка) --> "))
    if nextCoinIs == 0:
        theCoinsAreTails += 1
        coins -= 1
    elif nextCoinIs == 1:
        theCoinsAreEagles += 1
        coins -= 1
    else:
        print("Попробуйте еще раз")

if theCoinsAreTails > theCoinsAreEagles:
    print("Переверните все монеты с орлом - {}".format(theCoinsAreEagles))
else:
    print("Переверните все монеты с решкой - {}".format(theCoinsAreTails))

# ********************
# **** Задача 12: ****
# ********************
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
print("\n")
print("Петя, ты студент! Как я тебя понимаю:D")
firstGuessIsX = int(input("Вводи первое число: "))
secondGuessIsY = int(input("Вводи второе число: "))
hintSumOfBothNumbers = firstGuessIsX + secondGuessIsY # equal S
hintProdOfBothNumbers = firstGuessIsX * secondGuessIsY # equal P
# Kate is a pretty girl 100%
# natural numbers start from 1
# max call of recurcion in Python equal 1000 
# it doesn't work, 'cause the numbers might (1000, 1000)
if firstGuessIsX > 1000 or secondGuessIsY > 1000:
    print("Ты обманщик!")
else:
    x = 0 # doesn't matter
    y = 2
    flag = True
    while flag:
        x = hintProdOfBothNumbers // y
        if x + y == hintSumOfBothNumbers and x * y == hintProdOfBothNumbers:
            print(f"Петя загадал {x, y}, а Катя красотка!")
            flag = False # same as break
        else:
            y += 1 # increase by 1 to get next value for division

# ********************
# **** Задача 14: ****
# ********************
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
print("\n")
number = int(input("Введите степень для числа 2: "))
while number > 1:
    print("2^{} = {}".format(number, pow(2, number)))
    number -= 1