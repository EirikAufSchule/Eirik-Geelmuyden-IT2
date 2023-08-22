søtFrukt = ["eple", "appelsin", "mango"]
surFrukt = ["sitron", "ananas"]

brukerFrukt = (input("Skriv en frukt og se om den er søt eller sur: ")).lower()

fruktFunnet = False

for frukt in søtFrukt:
    if frukt == brukerFrukt: 
        print(f"{frukt.capitalize()} er en søt frukt.")
        fruktFunnet = True
for frukt in surFrukt:
    if frukt == brukerFrukt:
        print(f"{frukt.capitalize()} er en sur frukt.")
        fruktFunnet = True

if not fruktFunnet:
    print(f"Jeg vet ikke om {brukerFrukt} er en sur eller søt frukt")