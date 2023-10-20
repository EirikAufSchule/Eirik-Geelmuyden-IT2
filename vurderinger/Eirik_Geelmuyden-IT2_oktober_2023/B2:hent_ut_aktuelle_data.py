from operator import indexOf
import A2_lister_og_ordboker as data

varer = data.varer


def skrivProduktInfo(id):
    produkt = varer[id]
    if not id in list(varer.keys()):
        print("Fant ikke produktet i databasen")
        exit()

    print(f"ID:{id}")
    produkt_keys = list(produkt.keys())

    for key in produkt_keys:
        value = produkt[key]
        if isinstance(value, dict):
            print(f"{key}: ")
            for n in list(value.keys()):
                print(f"\t{n}: {value[n]}")

        elif isinstance(value, list):
            print(f"{key}: ")
            for n in value:
                print(f"\t{n}")

        else:
            print(f"{key}:{value}")


def nyPris(id, nyPris):
    varer[id]["pris"] = nyPris


def nyFarge(id, farge):
    farger = varer[id]["farger"]

    if nyFarge.lower() not in farger:
        farger.append(farge)


def fjernFarge(id, farge):
    farger = varer[id]["farger"]

    if farge in farger:
        farger.remove(farge)


def nyEgenskap(id, navn, egenskap):
    varer[id]["Tekniske egenskaper"][navn] = egenskap


""" keys = list(varer.keys())
for i in keys:
    skrivProduktInfo(i)
 """

keys = list(varer.keys())
farge = "grå"
for i in keys:
    if farge in varer[i]["farger"]:
        print(f"Varen med ID {i} kommer i grå farge")
