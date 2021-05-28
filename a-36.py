# argumenty funkcji -lista parametrów

def funkcja(arg1, arg2 = "World", *args, **kwargs):
    print(arg1, arg2, args, len(args), kwargs)
    for x in args:
        print(x)
    for x in kwargs.values():
        print(x)

funkcja("Hello") # argument przyjmuje wartość domyślną
funkcja("Hello", "Kacper") # ala przeciążenie funkcji
funkcja("Hello", "Kacper", "!", "&", autor="Kacper", rok=2021) #wywołujemy krotki na koniec 
# kwargs zapisywane jest w postaci słownika

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
