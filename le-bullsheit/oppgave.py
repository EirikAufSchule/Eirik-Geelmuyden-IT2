import datetime as dt
import time
from calendar import timegm
from color import *

class Oppgave:
    def __init__(self, tittel, info, deadline_dato=None, deadline_klokkeslett=None) -> None:
        self.tittel = tittel
        self.dato_laget = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.siden_epoch_opprettet = time.time()
        self.info = info

        if deadline_dato != None:
            utc_time = time.strptime(f"{deadline_dato} {deadline_klokkeslett}", "%Y-%m-%d %H:%M")
            self.deadline = timegm(utc_time)
        else:
            self.deadline = 0

    def __str__(self):
        if self.deadline != 0:
            deadline_str = " - innen " + dt.datetime.utcfromtimestamp(self.deadline).strftime('%Y-%m-%d %H:%M')
        else:
            deadline_str = " - ingen deadline"
        return f"{Color.BOLD}{self.tittel}{Color.END} - Opprettet {self.dato_laget}{deadline_str}\n\t{self.info}"

class SamarbeidsOppgave(Oppgave):
    def __init__(self, tittel, info, partnere, deadline_dato=None, deadline_klokkeslett=None) -> None:
        super().__init__(tittel, info, deadline_dato, deadline_klokkeslett)
        self.partnere = partnere

    def __str__(self):

        super().__str__()
        return f"    Samarbeidspartnere: {[self.partnere[i] for i in range(len(self.partnere))]}"
