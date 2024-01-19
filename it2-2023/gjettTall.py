import random

tilfeldigTall = random.randint(1,10)

gjett = int(input("Gjett heltallet (1-10): "))

if gjett > tilfeldigTall:
    print(f"Du gjettet for høyt. Det tilfeldige tallet var {tilfeldigTall}.")
elif gjett < tilfeldigTall:
    print(f"Du gjettet for lavt. Det tilfeldige tallet var {tilfeldigTall}.")
elif gjett == tilfeldigTall:
    print(f"Du gjettet for riktig! Det tilfeldige tallet er {tilfeldigTall}!")