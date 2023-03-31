def find_fractions(k):
    m = k * 2
    y = k + 1
    fr = []
    while y <= m:
        x = k * y / (y - k)
        if int(x) == x:
            fr.append([x,y])
        y += 1
    return fr

while True:
    try:
        k = int(input())
        fractions = find_fractions(k)
        print(len(fractions))
        for fraction in fractions:
            print(f'1/{k} = 1/{int(fraction[0])} + 1/{fraction[1]}')
    except EOFError:
        break