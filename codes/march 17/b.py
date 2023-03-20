while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    fa = input().split()
    da = {}
    for i in fa:
        if i in da.keys():
            da[i] += 1
        else:
            da[i] = 1
    fb = input().split()
    db = {}
    for i in fb:
        if i in db.keys():
            db[i] += 1
        else:
            db[i] = 1
    trade_a = 0; trade_b = 0
    for card in da:
        if card not in db.keys():
            trade_a += 1
    for card in db:
        if card not in da.keys():
            trade_b += 1
    print(min([trade_a, trade_b]))