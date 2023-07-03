t = int(input())

for _ in range(t):
    n = int(input())
    candies = [int(x) for x in input().split()]
    if sum(candies) % 2:
        print("NO")
        continue
    um = [x for x in candies if x == 1]
    dois = [x for x in candies if x == 2]
    if not len(um) and n % 2:
        print("NO")
    else:
        print("YES")