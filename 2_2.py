lst = input().split()
a = lst[1]
N = int(lst[0])
b = ""
for i in range(int(len(a)/N)):
    for j in range(N):
        b+=a[N*(i+1)-j-1]
print(b)