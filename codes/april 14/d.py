s = [int(x) for x in input().split()]
m = max(s)
s.remove(m)
print(m - s[0], m - s[1], m - s[2])