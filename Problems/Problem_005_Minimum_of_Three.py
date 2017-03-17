"""Даны несколько троек чисел. Требуется выбрать наименьшее в каждой тройке.

Входные данные - первая строка указывает количество троек чисел.
Каждая из следующих строк содержит одну такую тройку.
Ответ должен содержать выбранные из каждой тройки минимумы, по порядку, через пробел."""
n = int(input())
for i in range(n):
    line = input().split()
    if int(line[0])<int(line[1]) and int(line[0])<int(line[2]):
        print(line[0], end=' ')
    if int(line[1])<int(line[0]) and int(line[1])<int(line[2]):
        print(line[1], end=' ')
    if int(line[2])<int(line[0]) and int(line[2])<int(line[1]):
        print(line[2], end=' ')