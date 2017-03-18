n = int(input())
answ = []
for i in range(n):
    line = input().split()
    answ.append(str(round(float(line[0])/float(line[1]))))
print(' '.join(answ))