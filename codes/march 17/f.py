values = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}

while True:
    line = input()
    if line == '*':
        break
    measures = line.split('/')
    count = 0
    for measure in measures:
        duration = 0
        for m in measure:
            duration += values[m]
        if duration == 1:
            count += 1
    print(count)