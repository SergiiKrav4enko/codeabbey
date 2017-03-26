"""
Входные данные содержат одну строку из латинских букв и пробелов.
Ответ должен содержать строку такой же длины, но с символами в обратном порядке.
"""
line = list(input())
n = len(line) - 1
x = 0
for i in range(n):
    n_line = line.pop(n)
    line.insert(x, n_line)
    x += 1
print(''.join(line))