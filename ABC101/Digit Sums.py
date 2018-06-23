S = input()
x=0
for i in range(len(S)):
    x +=int(S[i])
if int(S) % x ==0:
    print('Yes')
else:
    print('No')