from statistics import *
import math

firstArray = [2, 4, 6, 8]
secondArray = [2, 4, 10, 12]

def getPiersonValue(firstArray, secondArray):
    firstMeanValue = mean(firstArray)
    secondMeanValue = mean(secondArray)
    topA = list(map(lambda x: x - firstMeanValue, firstArray))
    topB = list(map(lambda y: y - secondMeanValue, secondArray))
    topResult = sum([x * y for x, y in zip(topA, topB)])
    bottomResult = math.sqrt(sum([math.pow(x, 2) for x in topA])) * math.sqrt(sum([math.pow(y, 2) for y in topB]))
    print(f"Коэффициент корреляции Пирсона равен r = {topResult}/{bottomResult} = {topResult / bottomResult}")

getPiersonValue(firstArray, secondArray)