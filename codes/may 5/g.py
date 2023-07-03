t = int(input())

for _ in range(t):
    s = input()
    if len(set(s)) == 1:
        print(1 if s[0] == '0' else 0)
    else:
        if s[0] == '0':
            index = s.index('1')
            print(2 if '0' in s[index::] else 1)
        else:
            index = s.index('0')
            s = s[index::]
            if '1' in s:
                index = s.index('1')
                s = s[index::]
                if '0' in s:
                    print(2)
                else:
                    print(1)
            else:
                print(1)