land = {
    "kina": 1_439_324,
    "india": 1_380_004,
    "usa": 331_003,
    "indonesia": 273_524,
    "pakistan": 220_892
}

for navn in land:
    print(navn)

for innbyggere in land.values():
    print(innbyggere)

for navn, innbyggere in land.items():
    print(f"{navn.capitalize()} har {innbyggere} innbyggere")

land_sortert = sorted(land.keys())
print(land)

størst = 0
minst = land["kina"]
størst_navn = ""
minstnavn =""
for landnavn in land.keys():
    if land[landnavn] > størst:
        størst = land[landnavn]
        størst_navn = landnavn
    elif land[landnavn] < minst:
        minst = land[landnavn]
        minstnavn = landnavn

print("2", størst_navn)
print("1",minstnavn)