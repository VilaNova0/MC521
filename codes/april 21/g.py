def max_f(v, k):
    f = [0]
    for i in range(k):
        f.append(f[i] + v[i])
    return max(f)

t = int(input())

for _ in range(t):
    n = int(input())
    red = [int(x) for x in input().split()]
    m = int(input())
    blue = [int(x) for x in input().split()]

    print(max_f(red, n) + max_f(blue, m))