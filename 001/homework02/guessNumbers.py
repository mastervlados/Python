# ********************
# **** Задача 12: ****
# ********************
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# print("\n")
# print("Петя, ты студент! Как я тебя понимаю:D")
# firstGuessIsX = int(input("Вводи первое число: "))
# secondGuessIsY = int(input("Вводи второе число: "))
hintSumOfBothNumbers = 10 # equal S
hintProdOfBothNumbers = 25 # equal P
# Kate is a pretty girl 100%
# natural numbers start from 1
# max call of recurcion in Python equal 1000 
# it doesn't work, 'cause the numbers might (1000, 1000)
x = 0 # doesn't matter
y = 2
flag = True
step = 0
while flag:
    x = hintProdOfBothNumbers // y # :2 :3 :4 less
    step += 1
    if x + y == hintSumOfBothNumbers and x * y == hintProdOfBothNumbers:
        print(f"Петя загадал {x, y}, а Катя красотка!")
        flag = False # same as break
    else:
        y += 1 # increase by 1 to get next value for division
print(f"Она отгадала с {step} попытки!")
