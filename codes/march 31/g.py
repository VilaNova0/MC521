t = int(input())

for _ in range(t):
    n = int(input())
    start = 3
    curr=2
    while(True):
        if(n%start==0):
            print(int(n/start))
            break
        else:
            start+=2**curr
            curr+=1