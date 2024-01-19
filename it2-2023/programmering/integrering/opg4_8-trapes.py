
n = 1000
a = -1
b = 2
d = (b - a)/n

areal = 0

def f(x):
    return 3*x**2
x = a
for i in range(n):
    trapes = d*(f(x) + f(x+d))/2
    areal = areal + trapes
    x = x + d

print(areal)