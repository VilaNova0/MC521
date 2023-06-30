def multiply_every_n(v, k):
    res = []
    for i in range(k - 1, len(v) - k + 1):
        aux = v[k-i:k+i-1]
        if len(aux) == len(set(aux)):
            if k == 1:
                print("aux =", aux)
            mult = 1
            for a in aux:
                mult *= a
            res.append(mult)
    print("res =", res)
    return sum(res)

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    g = []
    while len(g) < n:
        g.extend([int(x) for x in input().split()])
    maximum = 0
    for k in range(1, n):
        fitness = multiply_every_n(g, k) % m
        print("k =", k, "fitness =", fitness)
        if fitness > maximum:
            maximum = fitness
    print(maximum)