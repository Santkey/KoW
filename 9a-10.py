#10 - funkcje cz.2

def funkcja(x):
    return x * x


zmienna = funkcja

#print(zmienna(5))

def funkcja2(f1, x):
    return f1(x) * x
#print(funkcja2(funkcja, 5))

def silnia(x):
    if x <= 1:
         return 1
    else:
        return x *silnia(x - 1)
print(silnia(10))

# silnia(3) = 3 * 2 * 1 = 6