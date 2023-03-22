n = int(input())

for i in range(n):
    c = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    d = []
    for j in range(3):
        d.append(c[j] - a[j])
    if d[0] < 0 or d[1] < 0 or d[2] < 0:
        print('no')
        continue
    if d[0] + d[2] < a[3]:
        print('no')
        continue
    if a[3] > d[0]:
        d[2] -= (a[3] - d[0])
    if d[1] + d[2] < a[4]:
        print('no')
        continue
    print('yes')