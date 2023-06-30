def v(l, n):
    for i in range(1, n):
        if l[i] - l[i - 1] > 1:
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(v(sorted(l), n))