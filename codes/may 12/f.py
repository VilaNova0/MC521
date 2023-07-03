t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    for i in range(n - 1):
        if not count % 2 and s[i] == '1' and s[i + 1] == '0':
            count += 1
        elif count % 2 and s[i] == '0' and s[i + 1] == '1':
            count += 1
    print(count)