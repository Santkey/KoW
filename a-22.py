# programowanie funkcyjne - generatory (yield)

def gen():
    i = 0
    while i < 5:
        yield i
        i += 1


for i in gen(): #iterowanie poprzez pętlę for
    print(i)

print(list(gen())) # tworzenie listy z podanymi liczbami

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i +=1
for i in parzyste(16):
    print(i)


print(list(parzyste(30)))
    