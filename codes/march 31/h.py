def less_sales(i, a):
    current = a[i]
    aux = 0
    for v in a[0:i]:
        if v <= current:
            aux += 1
    return aux

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = 0
    for i in range(1, n):
        b += less_sales(i, a)
    print(b)