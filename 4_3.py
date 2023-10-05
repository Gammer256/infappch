import matplotlib.pyplot as plt
f = open("iris_data.csv", "r")
lines = f.readlines()
print(lines)
lst = [0,0,0]
lst2 = [0,0,0]
names = ['Iris-setosa','Iris-versicolor' ,'Iris-virginica']
a = len(lines[1:])
for char in lines[1:]:
    if char.split(',')[5]=='Iris-setosa\n':
        lst[0]+=1/a
    elif char.split(',')[5]=='Iris-versicolor\n':
        lst[1]+=1/a
    elif char.split(',')[5]=='Iris-virginica\n':
        lst[2]+=1/a
    z=float(char.split(',')[3])
    if z<1.2:
        lst2[0]+=1/a
    elif z>=1.2 and z<=1.5:
        lst2[1]+=1/a
    elif z>1.5:
        lst2[2]+=1/a

fig = plt.figure(figsize = (8,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.pie(lst, labels = names)
ax1.set_title('Цветочки')
ax2.pie(lst2, labels = ['l<1.2','1.2<l<1.5','1.5<l'])
plt.show()
