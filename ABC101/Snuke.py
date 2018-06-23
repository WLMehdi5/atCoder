def sunuke(n):
    if (n / digit_sum(n)) > (n+1 / digit_sum(n+1)):
        return False
    return True


def digit_sum(S):
    x=0
    for i in range(len(str(S))):
        x +=int(str(S)[i])
    return x


K = input()
co = 0
for i in range(1,pow(10,15)):
    if sunuke(i) == True:
        print(i)
        co += 1
    if co >=int(K):
        break
