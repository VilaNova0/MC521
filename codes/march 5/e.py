def esq(linha, i):
    for j in range(i, 0, -1):
        if linha[j] == 'B':
            linha[j - 1] = 'R'
        else:
            linha[j - 1] = 'B'
    return linha

def constroi(n):
    l = []
    for i in range(n):
        l.append('B' if not i % 2 else 'R')
    return l

t = int(input())

for _ in range(t):
    n = int(input())
    linha = [x for x in input()]
    if linha == ['?'] * n:
        linha = constroi(n)
    else:
        i = 0
        while linha[i] == '?':
            i += 1
        if i > 0:
            linha = esq(linha, i)
        for j in range(i + 1, n):
            if linha[j] == '?':
                if linha[j - 1] == 'B':
                    linha[j] = 'R'
                else:
                    linha[j] = 'B'
    print(''.join(linha))