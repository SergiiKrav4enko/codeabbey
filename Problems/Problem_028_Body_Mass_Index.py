"""
Входные данные - указывают количество человек (подопытных!) в первой строке.
Остальные строки содержат параметры одного человека каждая - вес в килограммах и рост в метрах.
Ответ должен содержать одно из слов under, normal, over, obese (см. категории выше) для каждого из исследуемых людей, через пробел.
"""
n = int(input())
answer = []
for i in range(n):
    line = input().split()
    x = float(line[0])/(float(line[1])**2)
    if x < 18.5:
        answer.append('under')
    elif x >= 18.5 and x < 25.0:
        answer.append('normal')
    elif x >= 25.0 and x < 30.0:
        answer.append('over')
    else:
        answer.append('obese')
print(' '.join(answer))