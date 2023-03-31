t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    line = sorted([int(x) for x in input().split()])
    left = 0; right = n - 1; greater_r = 0
    while left < right:
        if line[left] + line[right] > r:
            right -= 1
        else:
            greater_r += right - left
            left += 1
    left = 0; right = n - 1; less_l = 0
    while left < right:
        if line[left] + line[right] > l - 1:
            right -= 1
        else:
            less_l += right - left
            left += 1
    print(greater_r - less_l)