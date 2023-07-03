t = int(input())

for _ in range(t):
    n = int(input())
    f = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    count = 0; last = n - 1

    for i in range(n - 1, -1, -1):
        if last < 0:
            break
        if f[i] == s[last]:
            count += 1
            last -= 1
    print(n - count)