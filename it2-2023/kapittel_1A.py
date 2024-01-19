import calendar as c
from math import sqrt

#print(c.month(2005,12))

"""
a = float(input("skriv første katetlengden: "))
b= float(input("skriv andre katetlengden: "))

c = sqrt(a**2 + b**2)

print("hypotenusen er ca.", round(c,2)) 
"""

""" 
tall1 = "100 m"
tall2 = "300 000 km/s"
tall3 = "2,718 281 828 459 045"

tall1 = tall1.replace("m", "")
print(int(tall1)*2)

tall2 = tall2.replace("km/s", "").replace(" ", "")
print(int(tall2)-1)

tall3 = tall3.replace(",",".")
tallListe = []
tallStart = 0
for i in range(len(tall3)):
    if tall3[i] == " ":
        tallListe.append(float(tall3[tallStart:i]))
        tallStart = i
    if i == len(tall3)-1:
        tallListe.append(float(tall3[tallStart:i+1]))
        tallStart = i
print(tallListe) 
"""
#alternativ løsning
""" tall3 = tall3.split(" ")
for i in range(len(tall3)):
    tall3[i] = float(tall3[i])
print(tall3) """

navn = "jakob"
alder = "urgammel"

print(f"navn:{navn:>15}\nalder:{alder:>14}")
