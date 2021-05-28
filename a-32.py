#wyrażenia regularne - Regular expressions (match, search)

import re #biblioteka regular

wzor = r"banan"
tekst = r"gruszkabananjabłkobananbanan"

print(re.match(wzor, tekst))

if re.match(r".*" + wzor + r".*", tekst): #match podaje czy wzór znajduje się w tekście na pierwszej pozycji
    print("Dopasowano!") 
else:
    print("Nie dopasowano")

if re.search(wzor, tekst): #search podaje czy wzór znajduje się w całośći tekstu
    print("Znaleziono!")
else:
    print("Nie dopasowano")

print(re.findall(wzor, tekst)) #znajduje wszystkie dopasowania wzoru w tekście i tworzy z nich listę

dopasowanie =re.search(wzor, tekst)
if dopasowanie:
    print(dopasowanie.group()) #zwraca szukany wzór
    print(dopasowanie.start()) #zwraca wartość gdzie zaczyna się szukany wzór
    print(dopasowanie.end()) #zwraca wartość gdzie kończy się szukany wzór
    print(dopasowanie.span()) #zwraca wartość gdzie zaczyna się i kończy szukany wzór zapisywane w krotce

tekst2 = re.sub(wzor, r"truskawka", tekst) #zamienia dopasowania w tekście ze wzoru na podany wyraz 
print(tekst2)


