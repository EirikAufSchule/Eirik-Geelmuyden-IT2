from math import cos, pi

a = 0
b = pi

n = 6
d = (b-a)/n


def f(x):
    return cos(x)

x=a 
integral = 0
for i in range(n):
    trapes = (f(x) + f(x + d))/2 * d 
    integral = integral + trapes
    x = x + d
    
print(integral)