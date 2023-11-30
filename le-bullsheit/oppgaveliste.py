#arv: spesialiserte lister, filmer

import datetime as dt
import time

from oppgave import *
##os varsler


class FeilInput(Exception):
    pass

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


class OppgaveListe():
    def __init__(self, lagrede_oppgaver = []):
        self.liste = lagrede_oppgaver

    def __str__(self):
        return_str = ""
        liste = list(self.liste )
        antall_sek_døgn = 86_400
        style = ""

        for i in range(len(liste)):
            tidssone_offset = 1
            if liste[i].deadline == 0:
                #print(f"{i+1}. {oppgaver[i].tittel}, opprettet [{oppgaver[i].dato_laget}]")
                return_str += f"{i+1}. {liste[i].tittel}, opprettet {liste[i].dato_laget}\n"

            else: 
                nå = time.time() + tidssone_offset
                if liste[i].deadline - nå < 0:
                    style = Color.RED
                elif liste[i].deadline - nå < antall_sek_døgn:  #heisann hoppsan jeg liker gutterompe an all dat 
                    style = Color.YELLOW

                deadline = dt.datetime.utcfromtimestamp(liste[i].deadline).strftime('%Y-%m-%d %H:%M')
                #print(f"{style}{i+1}. {oppgaver[i].tittel}, deadline {oppgaver[i].deadline}{Color.END}")
                return_str += f"{style}{i+1}. {liste[i].tittel}, deadline: {deadline}{Color.END}\n"

        return return_str

    def endre_prioritet(self):
        gammel_index = int(input("Hvilken oppgave vil du endre prioritet til (nr)? ")) - 1
        ny_index = int(input("Hva er den nye prioriteten (nr)? ")) - 1

        if gammel_index > len(self.liste) or ny_index > len(self.liste):
            raise FeilInput("Du må velge nr for en oppgave som eksisterer. ")
        #pop returnerer fjernet verdi
        self.liste.insert(ny_index, self.liste.pop(gammel_index))

    def endre_tittel(self):
        index = int(input("Hvilken oppgave vil du endre tittel på (nr)")) - 1
        forrige_tittel = self.liste[index].tittel
        ny_tittel = input(f"Hva er den nye tittelen til oppgave {index+1}?")
        self.liste[index].tittel = ny_tittel
        print(f"Tittel endret fra {forrige_tittel} til {ny_tittel}", end = "\n\n")

    def legg_til_oppgave(self):
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

            if deadline_dato != None:
                oppgave = Oppgave(tittel, info, deadline_dato, deadline_klokkeslett)
            else:
                oppgave = Oppgave(tittel, info)
            
            if prioritet != "":
                if not isinstance(prioritet, int):
                    raise FeilInput("Du må skrive inn et heltall")
                else:
                    index = prioritet -1
                    self.liste.insert(index, oppgave)

            else:
                self.liste.append(oppgave)

        if not input("Vil du legge til flere oppgaver? (y/n)") == "y":
            addNewTask = False
        return

    def sorter_etter_deadline(self):
        liste = self.liste
        uten_deadline = []
        for oppgave in liste:
            if oppgave.deadline == 0:
                uten_deadline.append(oppgave)
                liste.pop(liste.index(oppgave))
        liste.sort(key = lambda x: x.deadline)
        self.liste = liste + uten_deadline
        return

    def sorter_etter_oppretting(self):
        self.liste.sort(key = lambda x : x.siden_epoch_opprettet)
        return
    
    def les_info(self):
        vil_lese_mer = True
        while vil_lese_mer:
            index = int(input("Skriv nr. på oppgave du vil se info for: ")) - 1 
            print(self.liste[index])
            if input("Vil du lese flere? (y/n)") != "y":
                vil_lese_mer = False
                
    def slett_oppgave(self):
        print(self)
        index = int(input("Skriv nr på oppgaven du vil slette: ")) - 1
        try:
            self.liste.pop(index)
        except IndexError:
            raise FeilInput("Du må skrive inn nr for en eksisterende oppgave.")