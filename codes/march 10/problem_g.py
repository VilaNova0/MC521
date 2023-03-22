m = int(input())

for i in range(m):
    n, a, b = map(int, input().split())
    if a > n or a > b:
        print(1)
        continue
    if n % a:
        print(n // a + 1)
    else:
        print(n // a)