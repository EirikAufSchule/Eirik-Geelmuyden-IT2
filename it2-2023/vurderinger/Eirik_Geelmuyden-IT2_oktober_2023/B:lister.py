def finn_delelige_tall(liste, tall):
    print(f"Starter søket etter tall delbare på {tall}")
    deleligeTall = []
    for i in liste:
        if i % tall == 0:
            deleligeTall.append(i)
    return deleligeTall

hundre_tall = []
for i in range(1,101):
    hundre_tall.append(i)

print(f"Listen har {len(hundre_tall)} elementer.")

for i in finn_delelige_tall(hundre_tall, 7):
    print(i)


    