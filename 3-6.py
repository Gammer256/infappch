def nk(lsx, lsy):
    x=0
    y=0
    xy=0
    xx=0
    le=min([len(lsx),len(lsy)])
    for i in range(le):
        x += lsx[i] / le
        y += lsy[i] / le
        xy += lsx[i]*lsy[i]/le
        xx+= lsx[i]**2/le
    a=(xy - x * y) / (xx - x ** 2)
    b=y-a*x
    return a,b
print(nk([1,2,3,4,5,6,7],[2,2,2,2,2,2,2]))



