plik = open("text.txt", "r") #otwórz plik do odczytu
tekst = plik.read() #odczytaj plik
plik.close() #zamknij plik i zwolnij pamięć

def policz(txt, znak): #definicja funkcji, która zawiera 2 zmienne
    licznik = 0
    for z in txt: # dla zmiennej z w tekście
        if z == znak: # jeżeli podana zmienna zawiera się w tekście 
            licznik += 1 # dodaj do licznika 1
    return licznik #zwróc licznik

#print(policz(tekst.lower(), "z")) # funkca policz, która z tekstu wyszuka wystąpienia "a"

for z in "abcdefghijklmnoprstuwxyz":
    ile = policz(tekst.lower(), z)
    procent = 100 * ile / len(tekst)
    print("Znak " + "{0} - {1} - {2}%".format(z.upper(), ile, round(procent, 2)))