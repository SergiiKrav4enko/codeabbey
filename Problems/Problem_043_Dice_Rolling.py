"""
Входные данные содержат в первой строке число значений, которые нужно преобразовать.
Остальные строки содержат по одному вещественному случайному числу каждая (в виде 0.142857 и т.п.)
Ответ должен содержать числа от 1 до 6 для каждого из входных тестов, через пробел.
"""
x=int(input())
for i in range(x):
    line=float(input())
    points=line*6
    points=int(points)+1
    print(points, end=' ')