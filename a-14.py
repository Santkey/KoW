#podstawowe operacje na plikach
# w - write
# r - read
# a - append

plik = open("test.txt", "a")
if plik.writable():
    ile = plik.write(input("Wprowadź tekst do zapisu: ") + "\n")
    print("Zapisano: ", ile, "znaków")
plik.close()

plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość zapisanego pliku to: ")
    for l in plik:
        print(l)