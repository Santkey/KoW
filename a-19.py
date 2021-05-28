plik = open("text.txt", "r") #otwórz plik do odczytu
tekst = plik.read() #odczytaj plik
plik.close() #zamknij plik i zwolnij pamięć

def policz(txt, znak): #definicja funkcji, która zawiera 2 zmienne
    licznik = 0
    for z in txt: # dla zmiennej z w tekście
        if z == znak: # jeżeli podana zmienna zawiera się w tekście 
            licznik += 1 # dodaj do licznika 1
    return licznik #zwróc licznik

#print(policz(tekst.lower(), "z")) # funkca policz, która z tekstu 
# wyszuka wystąpienia "a"

for z in "abcdefghijklmnoprstuwxyz":  #dla zmiennej w liście 
    ile = policz(tekst.lower(), z)  # funckji ile przypisz funckję policz(tekst z malych liter, oraz zmienna z)
    procent = 100 * ile / len(tekst) #procent to wartość 100 pomnożona przez ilość wsyąpień danego znaku przez długość tekstu
    print("Znak " + "{0} - {1} - {2}%".format(z.upper(), ile, round(procent, 2))) #wypisz znak, ilość wystąpień oraz zaookrąglij wartość procentową

