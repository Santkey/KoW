#obsługa wyjątków try and except

x = 12
y = 2

try: #wypróbuj wykonać działanie x/y i wypisz ...
#    print(x  + "!")
    lista =[]
#  print(lista[0])
    print(x / y)
    print("Udane dzielenie")
except (ZeroDivisionError, TypeError, IndexError): #za wyjątkiem wystąpienia dzielenia przez zero
    print("Nastąpił jeden z 3 błędów")
except: #używany do obsługi wyjątków  
    print("Inny błąd")
finally:
    print("Zakończone")
#except TypeError:
#    print("Wystąpiły dwa typy danych")




