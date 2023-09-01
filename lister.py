liste = [1,3,6,2,4]
liste.append(7)
liste.insert(0, "helskotten")
print(liste)

liste.pop(0)
print(liste)

def insertionSort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j = j-1

        a[j+1] = key


insertionSort(liste)
print(liste)
#er den større eller mindre enn forrige, så forrige etter det til vi finner index
#fra denne indexen flytt bort til index 
