t = int(input())

for _ in range(t):
    a, b, p = map(int, input().split())
    line = input()
    cost = [0] * len(line)
    aux = line[-1]
    price = 0
    for i in range(len(line) - 2, -1, -1):
        if line[i] == aux:
            if price == 0:
                price = a if aux == 'A' else b
            cost[i] = price
        else:
            aux = line[i]
            price += a if line[i] == 'A' else b
            cost[i] = price
    for i in range(len(line)):
        if cost[i] <= p:
            print(i + 1)
            break