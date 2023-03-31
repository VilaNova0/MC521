t = int(input())


for _ in range(t):
    n = int(input()) 
    if n<=6:
        print(15)
    elif n<=8:
        print(20)
    elif n<=10:
        print(25)
    else:
        result=0
        a = n//6
        b = n%6
        if b==0:
            result=15*a
        elif b!=0 and b<=2:
            result=15*a+5
        elif b!=0 and b<=4:
            result=15*a+10
        else:
            result=(a+1)*15
        print(result)