print("Kolejność: ")
print ((2 + 2) * 2)

print("Dzielenie: ")
print(5 / 2)
print(5 // 2) #zwraca wartość int

print("Mnożenie: ")
print(2 * 3)
print(2 ** 3) #potęgowanie

print("Skrócone operatory: ")
x = 5
x = x + 1
print(x)
x += 1 #skrócony operator
print(x)

print("Konwersja: ")
#a = input("Podaj pierwszą liczbę: ") #input zwraca wartość w typie string
#b = input("Podaj drugą liczbę: ")
#print(a + b) #string + string (ciąg znakowy)

#print(int(a) + int(b)) #konwersja na typ całkowity (int)

#print(float(a) + float(b)) #konwersja na typ zmiennoprzecinkowy (float)

#konwersja typu int na string
y = 2
z = 2
print(str(y) + str(z))

del y #komenda del usuwa zmienną y
print(str(y) + str(z))