t = int(input())

for _ in range(t):
    n = int(input())
    f = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    
    count = 0
    for i in range(n):
        index = s.index(f[i])
        if index == i:
            if set(s[index::]) != set(f[i::]):
                count += 1
        elif len(list(set(s[index::]) - set(f[i::]))):
            count += 1
        
    print(count)