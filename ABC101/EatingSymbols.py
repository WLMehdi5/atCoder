S = input()
x=0
for i in range(len(S)):
    if S[i] == '+':
        x +=1
    else:
        x -=1
print(x)