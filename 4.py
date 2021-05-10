wiek = int(input("Podaj swój wiek: "))
kasa = int(input("Podaj ilość pieniędzy jaką posiadasz: "))

if kasa >= 20 and wiek >= 18:
    print("Możesz wejść")
elif kasa < 20 and wiek >= 18:
    print("Masz za mało środków")
elif kasa >= 20 and wiek < 18:
    print("Jesteś za młody")
elif kasa < 20 and wiek < 18:
    print("Masz za mało środków oraz jesteś za młody")    
else:
    print("Wystąpił błąd")