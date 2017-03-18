n = input().split()
answ = []
for i in range(int(n[0])):
    answ.append(str(round((int(n[i+1])-32)*(5/9))))
print(' '.join(answ))