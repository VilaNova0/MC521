t = int(input())

for _ in range(t):
    n = int(input())
    linha = [int(x) for x in input().split()]
    neg = [x for x in linha if x < 0]
    modulo = [abs(x) for x in linha]
    if not len(neg) % 2:
        print(sum(modulo))
    else:
        print(sum(modulo) - 2 * min(modulo))