while True:
    l = input()
    if l == '0 Fuel consumption 0':
        break
    event = l.split()
    consumo = []; dist = []
    leaks = 0; consumption = 0
    if event[1] == 'Fuel':
        consumption = int[event[3]]
        consumo.append(int(event[3]))
        if event[0] != '0':
            if len(dist):
                dist.append(int[event[0]] - dist[-1])
            else:
                dist.append(int[event[0]])
    elif event[1] == 'Goal':
        if len(dist):
            dist.append(int[event[0]] - dist[-1])
        else:
            dist.append(int[event[0]])
    elif event[1] == 'Leak':
        leaks += 1
        consumo.append(consumo[-1] + 1)
        if len(dist):
            dist.append(int[event[0]] - dist[-1])
        else:
            dist.append(int[event[0]])
    elif event[1] == 'Mechanic':
        leaks = 0
        consumo.append(consumption)