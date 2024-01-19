from re import T


følge_start = float(input("Hvilket tall begynner følgen på (a1)? "))

k = float(input("Med hvilken faktor øker tallfølgen for hvert tall (k)? "))

antall_ledd = int(input("hvor mange ledd vil du finne? "))

tallfølge = []
for n in range(1, antall_ledd+1):
    tall = følge_start * k**(n-1)
    tallfølge.append(tall)

print(tallfølge, sep="\t")