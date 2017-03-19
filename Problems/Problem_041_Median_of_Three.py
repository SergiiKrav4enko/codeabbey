"""
Входные данные - первая строка содержит количество тестовых наборов чисел.
Остальные строки содержат сами наборы (тройки) - по одной в каждой строке.
Ответ должен содержать медианы этих троек, разделенные пробелами.
"""
n = int(input())
for i in range(n):
    line = input().split()
    if int(line[0])<int(line[1]) and int(line[0])<int(line[2]):
        if int(line[1])<int(line[2]):
            print(line[1], end=' ')
        else:
            print(line[2], end=' ')
    elif int(line[1])<int(line[0]) and int(line[1])<int(line[2]):
        if int(line[0])<int(line[2]):
            print(line[0], end=' ')
        else:
            print(line[2], end=' ')
    elif int(line[2])<int(line[0]) and int(line[2])<int(line[1]):
        if int(line[0])<int(line[1]):
            print(line[0], end=' ')
        else:
            print(line[1], end=' ')