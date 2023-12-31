from curses import KEY_MARK
import pickle
import os
import time

from oppgaveliste import *
from color import *

def print_operasjoner(operasjoner):
    for i in range(len(operasjoner)):
        print(f"{i+1}. {operasjoner[i]}")

    print("")
    return

newpath = r"/Users/eirikgeelmuyden/Desktop/Eirik-Geelmuyden-IT2/le-bullsheit/oppgave_liste-objekter.pkl"
lagrede_oppgaver = []
if os.path.exists(newpath):
    with open("le-bullsheit/oppgave_liste-objekter.pkl", "rb") as inp:
            lagrede_oppgaver = pickle.load(inp)

    
oppgaver = OppgaveListe(lagrede_oppgaver)
operasjoner = ["Legg til oppgave", "Sorter etter deadline", "Sorter etter oppretting (først -> sist)",
               "Endre prioritet", "Endre tittel", "Les info for oppgave", "Slett oppgave", "Slett liste", "Avslutt og lagre"]


print(f"Dette er en oppgaveliste. Du har {len(oppgaver.liste)} oppgaver lagret: ")
if len(oppgaver.liste) == 0:
    print("Du har ingen oppgaver🤗👏 Nyt fritiden #🥩🤛🤛")
while True:
    print(oppgaver, end="\n")
    print("Hva vil du gjøre nå?")
    print_operasjoner(operasjoner)
    svar = input("Skriv tall til operasjon: ")
    print("")

    try:
        match svar:
            case "1":
                oppgaver.legg_til_oppgave()
            case "2":
                oppgaver.sorter_etter_deadline()
            case "3":
                oppgaver.sorter_etter_oppretting
            case "4":
                oppgaver.endre_prioritet()
            case "5":
                oppgaver.endre_tittel()
            case "6":
                oppgaver.les_info()
            case "7":
                oppgaver.slett_oppgave()
            case "8":
                oppgaver.tøm_liste()
            case "9":
                print("byebye")
                with open("le-bullsheit/oppgave_liste-objekter.pkl", "wb") as outp:
                    pickle.dump(oppgaver.liste, outp, pickle.HIGHEST_PROTOCOL)
                exit()
    except FeilInput as error:
        print(f"{Color.RED}{error}{Color.END}")
