a,b = map(int, input().split())
a1,b1=a,b
while a1!=0 and b1!=0:
    if a1>b1:
        a1=a1-b1
    else:
        b1=b1-a1
d=a1+b1

x,y=0,0
while True:

    x+=1
    y=(d-a*x)/b
    if (d-a*x)%b==0:
        print(x,y,d)
        break
    x=(-x)

    y=(d-a*x)/b
    if (d-a*x)%b==0:
        print(x,y,d)
        break
    x=(-x)





