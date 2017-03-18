n = int(input())
sum_n = []
for i in range(n):
    line = input().split()
    prom_sum = int(line[0])
    sum_sum = int(line[0])
    for j in range(int(line[2])-1):
        prom_sum = prom_sum+int(line[1])
        sum_sum = sum_sum + prom_sum
    sum_n.append(str(sum_sum))
print(' '.join(sum_n))
          