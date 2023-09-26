def hokuspokus(tekst:str, n:int) -> str:
  
  nytekst = ""
  """går tegn for tegn, gjør om til ascii verdien, øker med funksjonsparameter nr.2, og gjør så tilbake om til vanlig tegn"""
  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode += n
    nytekst += chr(tallkode)

  return nytekst

def simsalabim(tekst:str, n:int) -> str:
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode -= n
    nytekst += chr(tallkode)

  return nytekst