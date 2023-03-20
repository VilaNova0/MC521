def remove_real_coins(pos, real):
    aux = []
    aux.extend(pos)
    for coin in aux:
        if coin in real and coin in pos:
            pos.remove(coin)
    return pos

ORIGINAL_COINS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

n = int(input())

for _ in range(n):
    possible_coins = []; real_coins = []
    events = {'left': [], 'right': [], 'outcomes': [], 'interest': []}
    for i in range(3):
        left, right, outcome = input().split()
        events['left'].append(left)
        events['right'].append(right)
        events['outcomes'].append(outcome)
        if outcome == 'even':
            real_coins.extend(left)
            real_coins.extend(right)
            possible_coins = remove_real_coins(possible_coins, real_coins)
        else:
            possible_coins.extend([l for l in left if l not in real_coins and l not in possible_coins])
            possible_coins.extend([r for r in right if r not in real_coins and r not in possible_coins])
            events['interest'].append(i)
    possible_coins = remove_real_coins(possible_coins, real_coins)
    fake = possible_coins[0]
    weight = ''
    event = events['interest'][0]
    if fake in events['left'][event]:
        if events['outcomes'][event] == 'up':
            weight = 'heavy'
        else:
            weight = 'light'
    else:
        if events['outcomes'][event] == 'up':
            weight = 'light'
        else:
            weight = 'heavy'
    print(f'{fake} is the counterfeit coin and it is {weight}.')
    