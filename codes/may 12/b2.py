n = int(input())
s = list(map(int, input().split()))
soma = [0] * (n+1)

for i in range(n):
    soma[i+1] = soma[i] + s[i]

q = int(input())
left = []; right = []

for i in range(q):
    l, r = map(int, input().split())
    left.append(l)
    right.append(r)

for i in range(q):
    num = (soma[right[i]] - soma[left[i] - 1]) // 10
    print(num)