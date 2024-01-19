def sok_register(nr, sykler):
    return sykler[nr]

rammenr = ["WBK0132K", "VE01562512D", "S5A001234", "WN17632Z", "TA78317B", "ME7265T"]

sykler = {}

for nr in rammenr:
    print(f"Hvem eier sykkelen med rammenummeret {nr}?")
    navn = input("Navn")
    adresse = input("Adresse")
    sykler[nr] = navn, adresse

fortsettSok = True
while fortsettSok:
    sokeNr = input("Skriv inn rammenummeret du vil søke opp: ")
    try:
        eierInfo = sok_register(sokeNr, sykler)
        print(f"Syklen med rammenr {sokeNr} eies av {eierInfo[0]} som bor i {eierInfo[1]}.")
    except KeyError:
        print("Fant ikke rammenummeret i registeret. Husk å sjekke for feilskriving.")

    if input("Vil du søke et annet nummer (y/n)?") != "y":
            fortsettSok = False
