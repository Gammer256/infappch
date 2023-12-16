

#Я написал класс для векторов. Со сложением, вычитанием,
# скалярным произведением и умножением на число

class Vector():

    def __init__(self,x,y,z):
        for char in [x,y,z]:
            assert (type(char)== float) or (type(char)== int), "x,y,z must be numbers"
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self,other):
        xs = self.x + other.x
        ys = self.y + other.y
        zs = self.z + other.z
        return Vector(xs,ys,zs)

    def __sub__(self,other):
        return self+(other*(-1))

    def __mul__(self,other):
        if type(other) == Vector:
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        else:
            xs = self.x*other
            ys = self.y*other
            zs = self.z*other
            return Vector(xs,ys,zs)

    def __rmul__(self, other):
        if type(other) == Vector:
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        else:
            xs = self.x*other
            ys = self.y*other
            zs = self.z*other
            return Vector(xs,ys,zs)

#1. 1 Центр масс системы материальных точек.
n = int(input("Сколько точек: "))
lst = []
v0 = Vector(0,0,0)
M = 0
for i in range(n):
    (mass, x, y, z) = map(int,input().split())
    M+=mass
    v0 = v0 + mass*Vector(x,y,z)
v0 = v0*(1/M)
print("Координаты центра масс:", v0.x, v0.y, v0.z)









