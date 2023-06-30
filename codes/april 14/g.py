t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if n <= k:
        print(1)
    elif k == 1:
        print(n)
    else:
        result = n
        aux = False; aux2 = False
        for i in range(2, int(n ** (1/2)) + 1):
            if not n % i and i <= k:
                result = min(result, n // i)
            if not n % i and n // i <= k:
                result = min(result, i)
        print(result)