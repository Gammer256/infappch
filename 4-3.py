def tr(size,symb):
    for i in range(size):
        print((i+1)*symb)
    for i in range(size-1):
        print((size-i-1)*symb)
lst = input().split()
tr(int(lst[0]),lst[1])