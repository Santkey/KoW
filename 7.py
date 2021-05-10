zmienna = 1
zmienna2 = "Abc"

lista = [1, 2, "c", "d", "e", ] #LISTA

#print(lista[4]) #odwołanie do indeksu 4
lista[2] = 3 #zamiana wartości pod indeksem 2
#print(lista)

tekst = "Hello world"
#print(tekst[0])

#print(lista + ["f", "g", ]) #dodawanie wartości do listy
#print(lista * 2)

#print("Ilość elementów listy: ", len(lista)) #len zwraca ilość elementów listy

lista.append("f")
#print(lista)
lista.append(["g", "h", ]) #dołączenie zagnieżdżonej listy do listy
#print(lista[6][1]) #odwołanie do 6 indeksu listy (drugiej listy) oraz do jej indeksu pierwszego

lista.insert(3, 3)
#print(lista)

#print("Ilość wystąpień znaku w liście: ", lista.count(3)) #count zlicza ilośc wystąpień znaków w liście

#print("Index: ", lista.index("f")) #zwraca indeks elementu listy
#print("Index: ", lista.index(3)) #zwraca pierwszy indeks występujący w liście
lista.remove("f") #metoda remove usuwa podany element listy
#print(lista)

lista2 = [1, 20, 35, -5, 0]
print("Minimalna wartość z listy: ", min(lista2))
print("Maksymalna wartość z listy: ", max(lista2))
lista2.sort() #metoda sort sotuje listę od min do max
print(lista2)
lista2.reverse() #metoda odwraca listę
print(lista2)
lista2.clear()#metoda clear czyści listę z wszystkich wartości
print(lista2)