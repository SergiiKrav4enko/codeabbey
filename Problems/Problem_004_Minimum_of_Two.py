"""Наша задача - из двух чисел выбрать меньшее. Будут даны несколько пар чисел для более тщательной проверки.

Входные данные - в первой строке указано количество пар сравниваемых чисел.
Следующие строки содержат сами эти пары - по одной на строку.
Ответ должен содержать наименьшие элементы из каждой пары, через пробел."""
n = int(input())
for i in range(n):
    line = input().split()
    if int(line[0])<int(line[1]):
        print(line[0], end=' ')
    else:
        print(line[1], end=' ')