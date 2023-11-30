import datetime as dt
import time
from calendar import timegm

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


class Oppgave:
    def __init__(self, tittel, info, deadline_dato = None, deadline_klokkeslett = None) -> None:
        self.tittel = tittel
        self.dato_laget = dt.datetime.now()
        self.siden_epoch_opprettet = time.time()
        self.info = info

        if deadline_dato != None:
            utc_time = time.strptime(f"{deadline_dato}T00:{deadline_klokkeslett}.00Z", "%Y-%m-%dT%H:%M:%S.%fZ")
            self.deadline = timegm(utc_time)
        else:
            self.deadline = 0

    def __str__(self):
        if self.deadline != 0:
            deadline_str = " - innen " + dt.datetime.utcfromtimestamp(self.deadline).strftime('%Y-%m-%d %H:%M')
        else:
            deadline_str = " - ingen deadline"
        return f"{Color.BOLD}{self.tittel}{Color.END} – Opprettet {self.dato_laget}{deadline_str}\n\t{self.info}"




