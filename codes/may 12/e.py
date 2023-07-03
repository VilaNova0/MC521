def gas(cities, max_fuel):
    if max_fuel >= cities:
        return cities - 1
    if cities == max_fuel + 1:
        return max_fuel
    count = max_fuel
    togo = cities - max_fuel - 1
    price = 2
    for i in range(togo):
        count += price
        price += 1
    return count

n, v = map(int, input().split())
print(gas(n, v))