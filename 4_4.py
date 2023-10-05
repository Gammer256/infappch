import matplotlib.pyplot as plt
import numpy as np
f = open("iris_data.csv", "r")
lines = f.readlines()
print(lines)
lst = []
for char in lines[1:]:
    m = char.split(",")
    dab = [float(m[1]),float(m[2]),float(m[3]),float(m[4])]
    lst.append(dab)
lst.sort(key=lambda x: x[2])
xs = [char[2] for char in lst]
ys = [char[3] for char in lst]
plt.scatter(xs,ys, marker = '.')
x = [0, 9.0]
y = np.interp(x, xs, ys)
lal = ('b = '+ str(y[0])+'\nk = '+ str((y[1]-y[0])/x[1]))
print(lal)
plt.plot(x,y, 'r', label = lal)
plt.legend()
plt.show()
