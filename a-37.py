#rozpakowanie krotki oraz listy - unboxing

a, b = [2, 5] #przechowują wartości z krotki/słownika
print(a)
print(b)

x = 10
y = 20

x, y = y, x #zamiana wartość zmiennych

print(x)
print(y)

start, *wszytsko, koniec = (1, 2, 3, 4, 5, 6, 7) #zamiana w kolekcję listy
print(start)
print(wszytsko) #wszystko staje się listę
print(koniec)


