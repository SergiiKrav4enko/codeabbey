"""
Входные данные содержат длину массива в первой строке.
Значения массива следуют во второй строке, через пробел.
Ответ должен содержать единственное число - получившуюся чексумму.
"""
import math
n = int(input())
line = input().split()
result = 0
seed = 113
limit = 10000007
for i in range(n):
    result = (result + int(line[i])) * seed
    result = math.fmod(result, limit)
print(int(result))