def procura_50_00(n):
    p = -1
    for i in range(len(n) - 1, -1, -1):
        if n[i] == '0':
            p = i
            break
    for i in range(p - 1, -1, -1):
        if n[i] in ['0', '5']:
            return p, i
    return -1, -1

def procura_25_75(n):
    p = -1
    for i in range(len(n) - 1, -1, -1):
        if n[i] == '5':
            p = i
            break
    for i in range(p - 1, -1, -1):
        if n[i] in ['2', '7']:
            return p, i
    return -1, -1

t = int(input())

for _ in range(t):
    n = input()
    if not int(n) % 25:
        print(0)
    else:
        count = 0
        x, y = procura_50_00(n)
        w, z = procura_25_75(n)
        if not x == y == -1 and not w == z == -1:
            cortes_xy = (len(n) - x - 1) + (x - y - 1)
            cortes_wz = (len(n) - w - 1) + (w - z - 1)
            print(min(cortes_xy, cortes_wz))
        elif not x == y == -1 and w == z == -1:
            print((len(n) - 1 - x) + (x - y - 1))
        else:
            print((len(n) - 1 - w) + (w - z - 1))