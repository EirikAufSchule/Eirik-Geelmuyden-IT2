import datetime

def hentDato(fnr):
    dag = int(fnr[:2])
    maaned = int(fnr[2:4])
    aar = fnr[4:6]
    return [dag,maaned,aar]

def maanedStrDict(maaned):
    maaned = str(maaned)
    maanedDict = {
        "1":"januar",
        "2":"februar",
        "3":"mars",
        "4":"april",
        "5":"mai",
        "6":"juni",
        "7":"juli",
        "8":"august",
        "9":"september",
        "10":"oktober",
        "11":"november",
        "12":"desember" 
    } 
    return maanedDict[maaned]

def maanedStrMatch(maaned):
    
    match str(maaned):
        case "1":
            return "januar"
        case "2":
            return"februar"
        case "3":
            return "mars"
        case"4":
            return "april"
        case "5":
            return "mai"
        case "6":
            return "juni"
        case "7":
            return "juli"
        case "8":
            return "august"
        case "9":
            return "september"
        case "10":
            return "oktober"
        case "11":
            return "november"
        case "12":
            return "desember" 

def aarhundrePrefiks(aar):
    today = datetime.date.today()
    if int(aar) > today.year-2000:
        prefiks = "19"
    else:
        prefiks = "20"
    return prefiks + aar

def kjoenn(fnr):
    kjoenstall = int(fnr[8])
    if kjoenstall%2 == 0:
        return "kvinne"
    else:
        return "mann"

fodselsnr = "02068210793" #input("Skriv inn fødselsnummer: ")
if len(fodselsnr) != 11:
    exit()


dato = hentDato(fodselsnr)
dag = dato[0]
maaned = dato[1]
aar = dato[2]
print(f"Fødselsdatoen er {dag}.{maanedStrMatch(maaned)} {aarhundrePrefiks(aar)} ({kjoenn(fodselsnr)})")
