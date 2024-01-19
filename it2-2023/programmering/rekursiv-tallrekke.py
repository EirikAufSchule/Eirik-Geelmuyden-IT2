def a(n):
    if n-1 > 1:
        return 3*a(n-1)-2
    else:
        return 5

for i in range(8,0,-1):
    print(a(i))