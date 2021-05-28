#programowanie funkcyjne - lambda expressions - wyrażenia lambda

def funkcja(f, liczba): #deklaracja funckji z parametrem o zmiennej f oraz argumentem liczba
    return f(liczba) #liczba jest argumentem


print(funkcja(lambda x: x * x, 3)) #definicja funkcji lambda, w której zmienna z zostaje zmieniona na x*x dla liczby 3

def kwadrat(x): #definicja funkcji kwadrat dla x, która zwraca kwadrat parametru
    return x * x

print(kwadrat(5))

wyn = lambda y: y * y #def lambda dla y podaje jego kwadrat i przyjmuje argument przy jej wywołaniu
print(wyn(5))


wyn2 = (lambda y: y * y)(7) #inna forma definicji funkcji lambda
print(wyn2)

wyn3 = (lambda x, z: x * z)(7, 8) # definicji funkcji lambda dla dwóch zmiennych
print(wyn3)