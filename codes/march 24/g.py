t = int(input())

for _ in range(t):
    n = int(input())
    s = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]
    durations = [f[0] - s[0]]
    for i in range(1, n):
        if s[i] >= f[i - 1]:
            durations.append(f[i] - s[i])
        else:
            durations.append(f[i] - f[i - 1])
    print(' '.join(map(str, durations)))