n,k = map(int, input().split())
fib = [1,1]
for i in range(n):
    fib.append(fib[i]+fib[i+1])
print(fib)
def fiba(nin, kin):
    if nin == 0: return('a')
    if nin == 1: return ('b')
    if kin<fib[nin-2]:
        return fiba(nin-2, kin)
    else:
        return fiba(nin-1,kin-fib[nin-2])
print(fiba(n,k-1))






