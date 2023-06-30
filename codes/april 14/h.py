t = int(input())

for _ in range(t):
    n = int(input())
    values = [int(x) for x in input().split()]
    types = [int(x) for x in input().split()]
    if values == sorted(values):
        print("yes")
    elif len(set(types)) == 2:
        print("yes")
    else:
        print("no")