def roll_north(die):
    new_die = {**die}
    new_die['top'] = die['south']
    new_die['north'] = die['top']
    new_die['bottom'] = die['north']
    new_die['south'] = die['bottom']
    return new_die

def roll_south(die):
    new_die = {**die}
    new_die['top'] = die['north']
    new_die['north'] = die['bottom']
    new_die['bottom'] = die['south']
    new_die['south'] = die['top']
    return new_die

def roll_west(die):
    new_die = {**die}
    new_die['top'] = die['east']
    new_die['west'] = die['top']
    new_die['bottom'] = die['west']
    new_die['east'] = die['bottom']
    return new_die

def roll_east(die):
    new_die = {**die}
    new_die['top'] = die['west']
    new_die['west'] = die['bottom']
    new_die['bottom'] = die['east']
    new_die['east'] = die['top']
    return new_die

while True:
    tumbles = int(input())
    if not tumbles:
        break
    die = {'top': 1, 'north': 2, 'south': 5, 'west': 3, 'east': 4, 'bottom': 6}
    for t in range(tumbles):
        direction = input()
        if direction == 'north':
            die = roll_north(die)
        elif direction == 'south':
            die = roll_south(die)
        elif direction == 'west':
            die = roll_west(die)
        else:
            die = roll_east(die)
    print(die['top'])