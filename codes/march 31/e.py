def check_cube(n):
    cubes = {}
    i = 1
    while i ** 3 <= n:
        cubes[i ** 3] = i
        i += 1
    for cube in cubes:
        b = n - cube
        if b in cubes:
            return "YES"
    return "NO"

t = int(input())

for _ in range(t):
    x = int(input())
    print(check_cube(x))