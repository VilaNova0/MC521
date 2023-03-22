n = int(input())

for i in range(n):
    x = int(input())
    cont_3 = 0; cont_2 = 0
    y = x
    while not y % 3:
        y /= 3
        cont_3 += 1
    while not y % 2:
        y /= 2
        cont_2 += 1
    if cont_3 < cont_2 or y != 1:
        print(-1)
        continue
    double = cont_3 - cont_2
    aux = 0
    while x != 1:
        if not x % 6:
            x /= 6
            aux += 1
        elif double:
            x *= 2
            aux += 1
            double -= 1
        else:
            aux = -1
            break
    print(aux)