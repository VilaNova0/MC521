def resolve(f, s, n):
    for i in range(n):
        if f[i] and s[i]:
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())
    first = [int(x) for x in input()]
    second = [int(x) for x in input()]
    print(resolve(first, second, n))