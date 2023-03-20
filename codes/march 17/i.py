t = int(input())

for _ in range(t):
    w, n = map(int, input().split())
    truck = {'weight': 0, 'total_dist': 0, 'back_dist': 0}
    for i in range(n):
        dist, weight = map(int, input().split())
        truck['total_dist'] += (dist - truck['back_dist'])
        if weight + truck['weight'] > w:
            truck['total_dist'] += 2 * dist
            truck['back_dist'] = 0
            truck['weight'] = 0
        truck['back_dist'] = dist
        truck['weight'] += weight
        if truck['weight'] == w or i == (n - 1):
            truck['total_dist'] += truck['back_dist']
            truck['back_dist'] = 0
            truck['weight'] = 0
    print(truck['total_dist'])