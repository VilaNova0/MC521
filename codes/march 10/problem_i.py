def muda_linha(l, s):
    aberto = 0; fechado = 0
    for x in range(s):
        if l[x] == '(':
            aberto += 1
        else:
            fechado += 1
        if fechado > aberto:
            l = l[:x] + l[x+1:] + l[x]
            return l
    return 'true'

n = int(input())

for i in range(n):
    s = int(input())
    l = input()
    cont = 0
    while l != 'true':
        l = muda_linha(l, s)
        if l != 'true':
            cont += 1
    print(cont)
