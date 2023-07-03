t = int(input())

for _ in range(t):
    n = int(input())
    f = input()
    s = input()
    mex = 0
    continuar = False
    for c in range(n):
        if continuar:
            continuar = False
            continue
        if f[c] == s[c] == '1':
            if c + 1 < n:
                if f[c + 1] == '0' or s[c + 1] == '0':
                    continuar = True
                    mex += 2
        elif f[c] == s[c] == '0':
            if c + 1 < n:
                if f[c + 1] == s[c + 1] == '1':
                    continuar = True
                    mex += 1
            mex += 1
        else:
            mex += 2
    print(mex)