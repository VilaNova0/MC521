t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split(" ")))
    c0 = 0
    c1 = 0
    c2 = 0
    for i in range(n):
        if l[i]%3==0:
            c0+=1
        elif l[i]%3==1:
            c1+=1
        else:
            c2+=1
    aux = n/3
    d0 = c0-aux
    d1 = c1-aux
    d2 = c2-aux
    count = 0
    if d0<0:
        if d2>0:
            m=min(abs(d0),d2)
            count+=m
            d0+=m
        if d0<0:
            count+=abs(d0)*2
    if d1<0:
        if d0>0:
            m=min(abs(d1),d0)
            count+=m
            d1+=m
        if d1<0:
            count+=abs(d1)*2
    if d2<0:
        if d1>0:
            m=min(abs(d2),d1)
            count+=m
            d2+=m
        if d2<0:
            count+=abs(d2)*2
    print(int(count))