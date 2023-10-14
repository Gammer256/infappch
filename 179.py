
lst = list(map(str, input().split()))
lst0 = []

def sravni(a,b):
    if (int(a+b))>=(int(b+a)):
        return a
    else:
        return b
while len(lst)!=0:
    a = lst[0]
    for char in lst:
        a = sravni(a,char)
    lst0.append(a)
    lst.remove(a)
re = ''
for char in lst0:
    re+=char
print(int(re))