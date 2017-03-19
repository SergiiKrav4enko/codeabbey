"""
Входные данные - в первой строке указано количество строк подлежащих обработке.
Дальше следуют сами строки, состоящие только из маленьких английских (латинских) букв и пробелов.
Ответ должен содержать количество гласных для каждой строки.
"""
n = int(input())
otvet = []
glasnie = 'aouiey'
x = 0
for i in range(n):
    line = input()
    for j in range(len(glasnie)):
        for b in range(len(line)):
            if glasnie[j] == line[b]:
                x += 1
    otvet.append(str(x))
    x = 0
print(' '.join(otvet))