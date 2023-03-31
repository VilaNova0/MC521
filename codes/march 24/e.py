t = int(input())

for _ in range(t):
    n = int(input())
    points = [n * 3] * 3
    set_a = set([x for x in input().split()])
    set_b = set([x for x in input().split()])
    set_c = set([x for x in input().split()])
    for a in set_a:
        if a in set_b and a in set_c:
            points[0] -= 3
            points[1] -= 3
            points[2] -= 3
            set_b.remove(a)
            set_c.remove(a)
        elif a in set_b:
            points[0] -= 2
            points[1] -= 2
            set_b.remove(a)
        elif a in set_c:
            points[0] -= 2
            points[2] -= 2
            set_c.remove(a)
    for b in set_b:
        if b in set_c:
            points[1] -= 2
            points[2] -= 2
            set_c.remove(b)
    print(f'{points[0]} {points[1]} {points[2]}')