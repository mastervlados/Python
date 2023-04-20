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
# **** Задача 14: ****
# ********************
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
print("\n")
number = int(input("Введите степень для числа 2: "))
while number > 1:
    print("2^{} = {}".format(number, pow(2, number)))
    number -= 1