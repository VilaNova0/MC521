t = int(input())

for _ in range(t):
    n = int(input())
    p = int(input())
    l = list(map(int, input().split(" ")))
    aux = [False]*(n+1)
    aux[0] = True
    for i in range(p):
        for j in range(n-l[i], -1, -1):
            aux[j+l[i]] |= aux[j]
    if aux[n]:
        print("YES")
    else:
        print("NO")