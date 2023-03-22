n = int(input())

for i in range(n):
    m = int(input())
    s = sorted([int(y) for y in input().split()])
    cont = [0] * (m + 1)
    for x in s:
        cont[x] += 1
    maximo = max(cont)
    nao_zeros = 0
    for j in cont:
        if j:
            nao_zeros += 1
    if maximo < nao_zeros:
        print(maximo)
    elif maximo == nao_zeros:
        print(maximo - 1)
    else:
        print(nao_zeros)