t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = []
    aux = -1; index = 0
    for i in range(n - 1):
        if int(s[i]) == aux:
            res.append(index)
        else:
            res.append(i + 1)
            index = i + 1
        aux = int(s[i])
    print(*res)