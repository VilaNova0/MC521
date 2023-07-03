t = int(input())

for _ in range(t):
    n = int(input())
    h = [int(x) for x in input().split()]
    ones = len([x for x in h if x == 1])
    print(n - ones//2)