
def speedFromTime(distance,time):
    return distance/time

def checkSpeed(speed, limit):
    speed = speed*3.6
    if speed > limit:
        return False
    else: 
        return True


def main():
    validInput = False
    while not validInput:
        try:
            time = float(input("Hvor langt tid brukte du på å kjøre 3500 meter (s)? "))
            registreringsnummer = input("Hva er registreringsnummeret ditt? ")
            validInput = True
        except ValueError:
            print("Du kan kun skrive inn tall - ")
    speed = speedFromTime(3500,time) 
    if checkSpeed(speed, 80):
        print("Du lå ikke over fartsgrensen.")
    else:
        print(f"Bilen med registreringsnummer {registreringsnummer} lå over fartsgrensen, med en fart på {speed*3.6:2}km/t")
checkAgain = True
while checkAgain:
    main()
    if input("Vil du skjekke igjen (ja/nei) ").lower() == "nei":
        checkAgain = False