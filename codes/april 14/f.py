def v(n):
    if n % 4:
        return False
    l = []
    h = n // 2
    for i in range(1, h + 1):
        l.append(2 * i)
    soma_par = sum(l)
    aux = [(x - 1) for x in l]
    l.extend(aux)
    aux.pop()
    soma_impar = sum(aux)
    l[-1] = soma_par - soma_impar
    return l

t = int(input())

for _ in range(t):
    n = int(input())
    res = v(n)
    if res:
        print("YES")
        print(*res)
    else:
        print("NO")