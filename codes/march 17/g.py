from math import ceil

t = int(input())

for _ in range(t):
    piece, m, n = input().split()
    m = int(m); n = int(n)
    if piece in ['r', 'Q']:
        print(min(m, n))
    elif piece == 'k':
        if m*n % 2:
            print((m*n)//2 + 1)
        else:
            print((m*n // 2))
    else:
        print(ceil(m/2) * ceil(n/2))