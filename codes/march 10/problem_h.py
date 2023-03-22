def check(w, l):
    c = 0; count = 0
    while c < l:
        if not count % 2:
            c += 1
        else:
            if c+1 < l:
                if w[c] != w[c+1]:
                    return False
                else:
                    c += 2
            else:
                return False
        count += 1
    return True

n = int(input())

for i in range(n):
    l = int(input())
    w = input()
    if check(w, l):
        print('YES')
    else:
        print('NO')