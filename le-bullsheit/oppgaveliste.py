import datetime as dt
from calendar import timegm
import time
import pickle
##os varsler

#farge i forhold til deadline

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

oppgaver_liste = []
class Oppgave:

    def __init__(self, tittel, info, prioritet=-1, deadline_dato = None, deadline_klokkeslett = None) -> None:
        self.tittel = tittel
        self.dato_laget = dt.datetime.now()
        self.siden_epoch_opprettet = time.time()
        self.prioritet = prioritet
        self.info = info

        if deadline_dato != None:
            utc_time = time.strptime(f"{deadline_dato}T00:{deadline_klokkeslett}.00Z", "%Y-%m-%dT%H:%M:%S.%fZ")
            self.deadline = timegm(utc_time)
        else:
            self.deadline = 0

        if prioritet < 0 or prioritet > len(oppgaver_liste):
            oppgaver_liste.append(self)
        else:
            oppgaver_liste.insert(self, self.prioritet)


    def endre_tittel(self, ny_tittel, oppgaver):
        self.tittel = ny_tittel 
        print(f"Oppdatert oppgaveliste:")
        print_liste(oppgaver)

    def __str__(self):
        if self.deadline != 0:
            deadline_str = " - innen " + dt.datetime.utcfromtimestamp(self.deadline).strftime('%Y-%m-%d %H:%M')
        else:
            deadline_str = " - ingen deadline"
        return f"{Color.BOLD}{self.tittel}{Color.END} – Opprettet {self.dato_laget}{deadline_str}\n\t{self.info}"





def print_liste(liste):
    liste = list(liste)
    antall_sek_døgn = 86_400
    style = ""
    for i in range(len(liste)):
        if liste[i].deadline == 0:
            #print(f"{i+1}. {oppgaver[i].tittel}, opprettet [{oppgaver[i].dato_laget}]")
            print(f"{i+1}. {liste[i].tittel}, opprettet [{liste[i].dato_laget}]")

        else:   
            if liste[i].deadline - time.time() < 0:
                style = Color.RED
            elif liste[i].deadline - time.time() < antall_sek_døgn: 
                style = Color.YELLOW

            deadline = dt.datetime.utcfromtimestamp(liste[i].deadline).strftime('%Y-%m-%d %H:%M')
            #print(f"{style}{i+1}. {oppgaver[i].tittel}, deadline {oppgaver[i].deadline}{Color.END}")
            print(f"{style}{i+1}. {liste[i].tittel}, deadline: {deadline}{Color.END}")

    print("")


def endre_prioritet(liste, gammel_nr, ny_nr):
    gammel_index = gammel_nr
    index = ny_nr - 1
    #pop returnerer fjernet verdi
    liste.insert(index, liste.pop(gammel_index - 1))
    print(f"Oppdatert oppgaveliste:")
    print_liste(liste)
    return liste


def print_operasjoner(operasjoner):
    for i in range(len(operasjoner)):
        print(f"{i+1}. {operasjoner[i]}")

    print("")


def legg_til_oppgave():
    addNewTask = True
    deadline_dato = None
    deadline_klokkeslett = None

    while addNewTask:
        tittel = input("Angi tittel: ")
        info = input("Angi eventuell info: ")
        if input("Har oppgaven en deadline? (y/n)") == "y":
            deadline_dato = input("Skriv inn dato for deadline på formen år-måned-dag (xxxx-xx-xx): ")
            deadline_klokkeslett = input("Skriv inn tidspunkt for deadline på formen min:sek : ")
        
        prioritet = input("Skriv inn eventuell prioritet (1,2,3...). Ellers trykk enter: ")
        print(prioritet)
        if not isinstance(prioritet, int):
            prioritet = -1
        if deadline_dato != None:
            Oppgave(tittel, info,  int(prioritet) - 1, deadline_dato, deadline_klokkeslett)
        else:
            Oppgave(tittel, info, int(prioritet))
        
        if input("Vil du legge til flere oppgaver? (y/n)") != "y":
            addNewTask = False


def sorter_etter_deadline(liste):
    uten_deadline = []
    for oppgave in liste:
        if oppgave.deadline == 0:
            uten_deadline.append(oppgave)
            liste.pop(liste.index(oppgave))

    liste.sort(key = lambda x: x.deadline)
    return liste + uten_deadline

def sorter_etter_oppretting(liste):
    liste.sort(key = lambda x : x.siden_epoch_opprettet)
    return liste





with open("le-bullsheit/oppgave_liste-objekter.pkl", "rb") as inp:
    oppgaver_liste = pickle.load(inp)

print("Dette er et programmet er en to-do list. Begynn med å legge til en oppgave ")
legg_til_oppgave()

operasjoner = ["Legg til oppgave", "Sorter etter deadline", "Sorter etter oppretting (først -> sist)", "Endre prioritet","Les info for oppgave", "Slett oppgave", "Avslutt og lagre"]

while True:
    print("")
    print("Hva vil du gjøre nå?")
    print_operasjoner(operasjoner)
    svar = input("Skriv tall til operasjon: ")
    print("")

    match svar:
        case "1":
            legg_til_oppgave()
        case "2":
            oppgaver_liste = sorter_etter_deadline(oppgaver_liste)
            print_liste(oppgaver_liste)
            
        case "3":
            oppgaver_liste = sorter_etter_oppretting(oppgaver_liste)
            print_liste(oppgaver_liste)

        case "4":
            print_liste(oppgaver_liste)
            nr = int(input("Hvilken oppgave vil du endre prioritet til (nr)? "))
            ny_index = int(input("Hva er den nye prioriteten (nr)? "))
            oppgaver_liste = endre_prioritet(oppgaver_liste, nr, ny_index)
        case "5":
            vil_lese_mer = True
            while vil_lese_mer:
                index = int(input("Skriv nr. på oppgave du vil se info for: ")) - 1 
                print(oppgaver_liste[index])
                if input("Vil du lese flere? (y/n)") != "y":
                    vil_lese_mer = False
        case "6":
            print_liste(oppgaver_liste)
            index = int(input("Skriv nr på oppgaven du vil slette: ")) - 1
            oppgaver_liste.pop(index)
            print_liste(oppgaver_liste)
        case "7":
            print("byebye")
            with open("le-bullsheit/oppgave_liste-objekter.pkl", "wb") as outp:
                pickle.dump(oppgaver_liste, outp, pickle.HIGHEST_PROTOCOL)
            exit()


