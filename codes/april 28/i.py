def findmax(ps,ws,l,p,w,strength):
    global aux
    w += ws[l[-1]]
    if w > strength:
        if p > aux:
            aux = p
            return
        return
    p += ps[l[-1]]
    for i in range(len(ps)):
        if i not in l:
            l.append(i)           
            findmax(ps,ws,l,p,w,strength)
            l.pop()

t = int(input())

for _ in range(t):
    n = int(input())
    price = []
    weight = []
    for i in range(n):
        p, w = map(int, input().split())
        price.append(p)
        weight.append(w)
    g = int(input())
    total = 0
    for _ in range(g):
        strength = int(input())
        aux = 0
        for i in range(n):
            findmax(price,weight,[i],0,0, strength)
        total += aux
    print(total)