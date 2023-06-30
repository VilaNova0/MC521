t = int(input())

for _ in range(t):
    x = int(input())
    if not x % 11 or not x % 111:
        print("yes")
        continue
    if x < 111:
        print("no")
        continue
    print("yes" if x >= 111 * (x % 11) else "no")