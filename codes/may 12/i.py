while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    tab = [[1] * k] * n
    for j in range(k):
        tab[0][j] = j + 1
    for i in range(1, n):
        for j in range(1, k):
            tab[i][j] = tab[i][j - 1] + tab[i - 1][j]
    print(tab[n - 1][k - 1] % 1000000)