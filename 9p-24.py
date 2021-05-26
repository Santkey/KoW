#zbiory - sets

liczby1 = {0, 1, 2, 4} #zbiór zapisujemy w nawiasach klamrowych (słownik),a wartości jak w liście
slowa = set(["a", "b", "c"]) #zbiór zapisuje się w nawiasach okrągłych oraz wew. kwadratowych, 
#a każda wartość jest unikalna


print(liczby1)
print(slowa)


liczby1.add(5) #dodawnie wartości
print(liczby1)

liczby1.remove(0) #usuwanie wartości
print(liczby1)

liczby1.pop() #usunięcie pierwszej wartości
print(liczby1)

liczby1.clear() #wyczyszczenie zbioru
print(liczby1)

print(1 in liczby1) #zapytanie czy dana wartość występuje w zbiorze
print("a" in liczby1)
print("a" in slowa)

liczby1 = {0, 1, 2, 3, 4}
liczby2 = {3, 4, 5, 6}

print(liczby1 | liczby2) #wypisuje sumę dwóch zbiorów bez powtórzeń i tworzy nowy zbiór

print(liczby1 & liczby2) #wypisuje wartości, które się powtarzają w obu zbiorach i tworzy nowy zbiór

print(liczby1 - liczby2) #wypisuje różnicą zbioru liczby1  do liczby2

print(liczby1 ^ liczby2) #wypisuje wartości, które są unikalne (koniunkcja)