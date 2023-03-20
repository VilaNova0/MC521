game = {'paper': 'rock', 'rock': 'scissors', 'scissors': 'paper'}
jafoi = False

while True:
    line = input()
    if line == '0':
        break
    if jafoi:
        print()
    n, k = map(int, line.split())
    players = []
    for i in range(n):
        players.append({'w': 0, 'l': 0})
    total = (k * n * (n-1) // 2)
    for play in range(total):
        p1, h1, p2, h2 = input().split()
        if h1 == h2:
            continue
        if game[h1] == h2:
            players[int(p1) - 1]['w'] += 1
            players[int(p2) - 1]['l'] += 1
        else:
            players[int(p2) - 1]['w'] += 1
            players[int(p1) - 1]['l'] += 1
    for player in players:
        if sum(player.values()):
            value = player['w'] / sum(player.values())
            print(f'{value:.3f}')
        else:
            print('-')
    jafoi = True