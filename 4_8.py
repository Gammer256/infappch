a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(*a)
print(*b)
print(*(a|b))
print(*(a&b))