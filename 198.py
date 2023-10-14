lst = list(map(int, input().split()))
n = len(lst)
lsr = [0]*n

lsr[0] = lst[0]
lsr[1] = max(lst[0], lst[1])
for i in range(n):
    lsr[i] = max(lst[i] + lsr[i - 2], lsr[i - 1])
print(lst[-1])
