# list comprehension , string formatter

lista = list(range(10))

#print(lista)

nowa = [i * 2 for i in lista] # mnożenie każdej wartości w liście 2 razy
nowa2 = [i + 1 for i in lista if i % 2 == 0]
print("Stara lista: ", lista)
print("Nowa lista: ", nowa)
print("Nowsza lista: ", nowa2)


#formatowanie string

argumenty =["Kacper", 21]
tekst = "Cześć, mam na imię {imie} i mam {wiek} lat.".format(imie=argumenty[0],wiek=argumenty[1])
print(tekst)