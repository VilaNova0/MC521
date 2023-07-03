n = int(input())
possibles = [int(x) for x in input().split()]
possibles.pop(0)
for _ in range(n - 1):
    line = [int(x) for x in input().split()]
    line.pop(0)
    possibles = [x for x in line if x in possibles]
print(*possibles)