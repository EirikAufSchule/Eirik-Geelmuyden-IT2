def figur(x):
    return 2*x**2+2*x

stikker = 10_000
figurer = 0 
brukt = 0

while stikker - figur(figurer+1) > 0:
    figurer = figurer + 1
    stikker = stikker - figur(figurer)

print(figurer)
print(stikker-brukt)