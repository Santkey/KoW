#programowanie funkcyjne - mapa i filtr (map & filter)

liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,] #zapisanie listy wartościami

# Mapy

def funkcja(x):   #stworzenie definicji funkcji, która mnoży wartości 2 razy
    return x * 2

wynik = map(funkcja, liczby) #stworzenie mapy, która wykorzystuje "funkcję" oraz podane "liczby"
print(list(wynik)) #drukuje w postaci listy wynik

wynik2 = map(lambda x: x * 2, liczby) #stworznie funkcji lambdy
print(list(wynik2))

# filtry

wynik3 = filter(lambda x: x % 2 == 0, liczby)
print(list(wynik3))

