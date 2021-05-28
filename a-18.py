#operacje na tekście i listach

print(", ".join(["a", "b", "c"])) #metoda join rozdziela podane elementy listy

print("Witaj Świecie".replace("Witaj", "Żegnaj")) #metoda replace zamienia pierwszy element z drugim

print("To jest zdanie".startswith("To")) #metoda startswith zwraca boolean(czy zaczyna się od?)

print("To jest zdanie".endswith("zdanie")) #metoda startswith zwraca boolean(czy kończy się na?)

print("j" in "To jest zdanie") #sprawdza czy wyrażenie znajduje się w zmiennej typu string

print("To jest zdanie".upper()) #zmienia znaki na duże

print("TO JEST ZDANIE".lower())# zmienia znaki na małe

print("------------")

lista = [10, 20, 30, 30, 40]

if all([i % 2 == 0 for i in lista]): #sprawdza czy wszystkie zmienne w liście spełniają podane warunki
    print("Wszystkie parzyste")
else:
    print("Coś nie jest parzyste")

if any([i % 2 == 1 for i in lista]): #sprawdza czy jakakolwiek zmienna w liście spełnia podany warunek
    print("Występuję przynajmniej jedna nieparzysta wartość")
else:
    print("Nie ma nieparzystych liczb w liście")    

for i in enumerate(lista): # funckja enumerate tworzy pary zmiennych, gdzie pojawia się indeks zmiennej i jej wartość 
    print(i[0] + 1, "-", i[1])


