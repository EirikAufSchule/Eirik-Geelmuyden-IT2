def hokuspokus(tekst, n):
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode += n
    nytekst += chr(tallkode)

  return nytekst

def simsalabim(tekst, n):
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode -= n
    nytekst += chr(tallkode)

  return nytekst