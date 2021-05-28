# słownik kolekcja -dictionary

slownik = {1: "Poniedziałek", 2: "Wtorek", 3: "Środa", 4: "Czwartek", 5: "Piątek"}

slownik[6] = "Sobota"

print(slownik)

slownik["a"] = 1

print(slownik["a"])
print(slownik)

#print(slownik[8])
print(slownik.get(8, " Inny dzień"))


#for l in slownik: #iterowanie po kluczach słownika
    #print (l)

#for d in slownik: # iterowanie po zawartości słownika
    #print(slownik[d])

print(slownik.pop(1))