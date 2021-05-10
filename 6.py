from random import randint

los = randint(1, 1000)
odp = -1
i = 0
print("Zgadnij liczbę  z przedziału 1-10")


while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Zgadywana liczba jest mniejsza")
    elif odp < los:
        print("Zgadywana liczba jest większa")
    elif odp == los:
        print("Brawo, wygrałeś za", i, "razem")
    
