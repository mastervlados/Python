# *******************
# **** Задача 2: ****
# *******************
# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 
def getSumDigitsOfThreeDigitNumber(number):
    
    result = 0
    digit  = 0

    if number > 99 and number < 1000:
        for i in range(3): # [0, 1, 2] 3 times
            digit = number % 10
            number //= 10
            print(" > ", digit)
            result += digit # sum++
        print(result)
    else:
        print(f"Функция не может обработать {number}.")
    # get the sum of digits for third task
    return result

getSumDigitsOfThreeDigitNumber(123)
getSumDigitsOfThreeDigitNumber(100)

# *******************
# **** Задача 4: ****
# ******************* 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
print("\n")
def origami(s):
    if s % 2 == 0:
        result = int(s / 2 // 3) 
        # :2 to find a half
        # :3 to get count of any boy
        print("{} --> {} {} {}".format(s, result, result * 4, result))
    else:
        print("Посчтитайте количество журавликов еще раз..")

origami(6)
origami(24)
origami(60)
origami(3)
# *******************
# **** Задача 6: ****
# ******************* 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
print("\n")
def noItCostsAlotForMe(ticketNumberToBeLucky):
    answer = "no"
    # we get sum from the first tack of this homework, just call method
    ticketFirstThreeDigitSum = getSumDigitsOfThreeDigitNumber(ticketNumberToBeLucky // 1000)
    ticketLastThreeDigitSum = getSumDigitsOfThreeDigitNumber(ticketNumberToBeLucky % 1000)
    if ticketFirstThreeDigitSum == ticketLastThreeDigitSum:
        answer = "yes"
    print("{} --> {}".format(ticketNumberToBeLucky, answer))

noItCostsAlotForMe(385916)
noItCostsAlotForMe(123456)
# *******************
# **** Задача 8: ****
# *******************
# Требуется определить, можно ли 
# от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
print("\n")
print("Возьми шоколадку в руку и не ешь пока, скажи мне:")
n = int(input("Сколько долек по вертикали: "))
m = int(input("Сколько долек по горизонтали: "))
k = int(input("Have no idea, just type number here: "))
answer = "no"

if k < m * n and (k % m == 0 or k % n == 0):
    answer = "yes"

print("{} {} {} --> {}".format(n, m, k, answer))