while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    heads = []; knights = []
    for _ in range(n):
        heads.append(int(input()))
    for _ in range(m):
        knights.append(int(input()))
    if n > m:
        print("Loowater is doomed!")
    elif min(heads) >= max(knights):
        print("Loowater is doomed!")
    else:
        go = 0
        heads = sorted(heads)
        knights = sorted(knights)
        while heads and knights:
            if heads[0] > knights[0]:
                knights.pop(0)
            else:
                go += knights.pop(0)
                heads.pop(0)
        if not heads:
            print(go)
        else:
            print("Loowater is doomed!")