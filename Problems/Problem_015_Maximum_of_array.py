n = input().split()
max_min = []
max_n = (n[0])
min_n = (n[0])
for i in range(len(n)):
    if int(max_n) < int(n[i]):
        max_n = (n[i])
    if int(min_n) > int(n[i]):
        min_n = (n[i])
max_min.append(max_n)
max_min.append(min_n)
print(' '.join(max_min))