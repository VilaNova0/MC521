def procura_vert(mat, x, y):
    for i in range(x, len(mat)):
        if mat[i][y] != 0:
            return mat[i][y]

def procura_hor(mat, x, y):
    for i in range(y, len(mat[x])):
        if mat[x][i] != 0:
            return mat[x][i]

n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for y in range(n)]

ceros = []
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 0:
            ceros.append([x, y])

for x in ceros[::-1]:
    vert_max = procura_vert(matrix, x[0], x[1])
    hor_max = procura_hor(matrix, x[0], x[1])
    if hor_max < vert_max:
        matrix[x[0]][x[1]] = hor_max - 1
    else:
        matrix[x[0]][x[1]] = vert_max - 1

aux = True
for x in matrix:
    for y in range(1, m):
        if x[y] <= x[y-1]:
            print(-1)
            aux = False
            break
    if not aux:
        break
if aux:
    for x in range(1, n):
        for y in range(m):
            if matrix[x][y] <= matrix[x-1][y]:
                print(-1)
                aux = False
                break
        if not aux:
            break

if aux:
    soma = 0
    for i in matrix:
        soma += sum(i)
    print(soma)