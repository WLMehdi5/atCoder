N, K = input().split()
lines = []
lines.append(input().split())
if int(K)%int(N) ==0:
    a = int(N)/int(K)
else:
    a = int(N)/int(K)+1
print(int(a))