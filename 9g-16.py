#krotka (kolekcja), wycinki

#tuple = krotka
#krotka != lista, ponieważ tupla jest nieedytowalna

krotka = (2, 4, 8, 16, 32, 64, 128,)

#print(krotka[0])
#print(krotka)
 #krotka[0] = 1

#for l in krotka:
#    print(l)

#print("Elemtów: ", krotka.count(l)) #ile elementów wystąpiło

#print("Index: ", krotka.index(64)) # zwraca indeks, pod którym znajduje się element

print("\nWycinki: ")
print(krotka[0:3]) #wypisz wartości spod indeksów 0 do 3(wyłącznie)
print(krotka[3:5]) #wypisz wartości spod indeksów od 3 do 5(wyłącznie)
print(krotka[3:]) #wypisz wartości spod indeksów od 3 do końca
print(krotka[-4:-2])
print(krotka[0:7:2])
print(krotka[::-1]) #wypisz wartości od końca