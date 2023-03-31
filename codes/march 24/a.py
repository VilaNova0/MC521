t = int(input())

for _ in range(t):
    n = int(input())
    line = input().split()
    st = set()
    aux = 0
    for i in line[::-1]:
        if i in st:
            break
        st.add(i)
        aux += 1
    print(n-aux)