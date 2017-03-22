"""
Входные данные в первой строке содержат количество списков.
Остальные строки содержат по одному списку чисел каждая.
Числа в каждом списке целые и положительные. Конец списка отмечен значением 0 - его не нужно включать в расчеты!!!
Ответ должен содержать средние значения для каждого из списков, округлённые до ближайшего целого (см задачу на округление), разделенные пробелами.
"""
n = int(input())
answer = []
for i in range(n):
    line = input().split()
    x = 0
    for j in range(len(line)):
        x += int(line[j])
    avg = x/(len(line)-1)
    answer.append(str(round(avg)))
print(' '.join(answer))