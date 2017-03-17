# Требуется найти сумму нескольких чисел (больше чем двух)
n = int(input())
chisla = input().split()
summa =0
for i in chisla:
    summa += int(i)
print(summa)