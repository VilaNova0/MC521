t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for i in range(k):
        if max(b) > min(a):
            max_b = b.index(max(b))
            min_a = a.index(min(a))
            aux = a[min_a]
            a[min_a] = b[max_b]
            b[max_b] = aux
    print(sum(a))