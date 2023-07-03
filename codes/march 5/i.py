def shop(m, costs):
    minimo = 0
    minimo += min(c for c in costs)
    if minimo > m:
        return "no solution"
    maximo = 0
    maximo += max(c for c in costs)


t = int(input())

for _ in range(t):
    m, c = map(int, input().split())
    costs = []
    for x in input().split():
        costs.append([int(x)])
        costs.pop(0)
    for i in range(1, c):
        inp = [int(x) for x in input().split()]
        inp.pop(0)
        costs.append(list(set(inp)))
    shop(m, costs)