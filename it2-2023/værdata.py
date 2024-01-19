dagNavn = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
regn = []
vind = []
temperatur = []

for i in range(7):
    validType = False
    while not validType:
        try:
            regn.append(float(input(f"Hvor mye regn var det på {dagNavn[i]} (mm)? ")))
            vind.append(float(input(f"Hva var vindstyrken på {dagNavn[i]}? (m/s)")))
            temperatur.append(float(input(f"Hva var temperaturen på {dagNavn[i]}? (c)")))
            print("")
            validType = True
        except ValueError:
            "Du må skrive inn et tall - "
målinger = [regn, vind, temperatur, "regn", "vind", "temperatur"]
for i in range(3):
    liste = målinger[i]
    avg = sum(liste)/len(liste)
    print(f"Gjennomsnitts{målinger[i+3]} for uken var {avg:.2f}")