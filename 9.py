def funkcja_test():
    print("Funkcja...")

#funkcja_test()

def dodaj(x):
    print(x + 1)

zmienna = dodaj(2)
print(zmienna)

def dodaj(x, y = 1, z = 0):
    return x + y + z

#dodaj(2, 3)
#(dodaj(2)
#(2, 5, 7)

print(dodaj(2, 3))
print(dodaj(2))
wynik = dodaj(2, 5, 7)
print(wynik)