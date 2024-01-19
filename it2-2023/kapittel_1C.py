'''
sum=0

rangeLmtr = 75
for i in range(50,rangeLmtr+1):
    sum+=i
print(f"Sum: {sum}")
print(f"Gjennomsnitt: {(sum/rangeLmtr)}")
'''

'''
for i in range(1,11):
    print("|", end = "")
    for j in range(1,11):
        print(f"{j*i:5}", end = "")
    print("")
    print("|")
'''

'''
for i in range(1,4):
    for j in range(1,6):
        print("#",end = "")
    print("")
'''


'''
maanednr = input("Oppgi nummeret til måneden vi er i: ")
gyldig = False
while not gyldig:
    try:
        maanednr = int(maanednr)
        if not (maanednr >= 1 and maanednr <= 12):
            maanednr = int(input("Heltallet må være mellom 1 og 12: "))
            gyldig = False
            gyldig = True
    except ValueError:
        maanednr = int(input("Du må skrive inn et heltall: "))

        
print("Du skrev inn et tall mellom 1 og 12 ")
'''

'''
snitt = input("oppgi karaktersnitt: ")
gyldig= False

while not gyldig:
    try:
        snitt = float(snitt)
        if snitt <= 6.4:
            gyldig = True
        else:
            snitt = input("Det må være et gyldig karaktersnitt (0 t.o.m. 6): ")
            gyldig = False
    except ValueError:
        snitt = input("Du må skrive inn et desimaltall: ")
print("weak")
'''

'''
liste = ["haha", 3,4, "haha"]

if "haha" in liste:
    print("'haha' eksisterer")
print(liste.index("haha"))#finner første instans av "haha"

print(liste.index("haha", 1))#leter fra og med 1
'''

'''
tallListe = list(range(1,21))

for tall in tallListe:
    if tall%2 == 0:
        fjernIndeks = tallListe.index(tall)
        tallListe.pop(fjernIndeks)
print(tallListe)


tallListe2 = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
leteStart = 0
tallFunnet = False
while not tallFunnet:
    if 3 in tallListe2:
        leteStart = tallListe2.index(3, leteStart)
        tallListe2.pop(leteStart)
    else:
        tallFunnet = True
print(tallListe2)
'''
import numpy as np 

liste = list(input("skriv inn tre tall"))
for i in liste:
    print(i)
