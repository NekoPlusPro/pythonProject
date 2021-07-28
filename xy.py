import math as m
pi=3.1415926/180
x1=114.360123*pi
y1=30.578962*pi
x2=114.39305*pi
y2=30.511181*pi
r=6371.0
d=r*m.acos(m.cos(y1)*m.cos(y2)*m.cos(x1-x2)+m.sin(y1)*m.sin(y2))
print (d)