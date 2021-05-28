# do powtórzenia

#wyrażenia regularne 4 - grupy walidacja e-mail

import re

wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+(!|.)$","Hello World World World&") # (nawiasy) stanowią grupę
#jeżeli w tekscie znajduje się wzór i jest on w grupach to wypisywane są całe grupy

# etykieta-label w grupie (?P<first>ll) - first to nazwa etykiety
# (?:He) - nie jest tworzony nowy indeks i etykieta nie ma nazwy
# (!|.) wykrzyknik dopuszczalny
# wykrzyknik dopuszczalny lub kropka (!|\.)

#if wynik:
    #print("Dopasowano!")
    #print(wynik.group(0))
    #print(wynik.group(1))
    #print(wynik.group(2))
    #print(wynik.group(3))
    #print(wynik.groups()) #tworzy krotkę
    #print(wynik.group("first")) #wywołanie po etykiecie

#else:
#   print("Nie dopasowano")

#walidacja adresu email

if re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.])+[A-Za-z0-9])@([A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9]\.[A-Za-z])$", "kacper.sanktiewicz@gmail.com"):   
    print("Dopasowano!")
    
else:
    print("Nie dopasowano")