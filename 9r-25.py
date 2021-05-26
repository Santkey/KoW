#programowanie obiektowe - Object oriented programming

#jeżeli funkcja znajduje się w klasie nazywa się ją METODĄ

class Czlowiek: #klasy zapisujemy od dużej litery 
    def __init__(self, imie, wiek): #metoda init jest konstruktorem 
        self.imie = imie
        self.wiek = wiek
    
    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imię " + self.imie + " i mam " + str(self.wiek) + " lat."

obiekt = Czlowiek("Sebastian", 25) #obiekt przechowuje klasę człowiek
print(obiekt.imie)
print(obiekt.przedstawSie("Witam")) #wywołujemy metodę przedstawSie bez argumentów

obiekt2 = Czlowiek("Adrian", 24)
obiekt2.imie = "Adrian"
print(obiekt2.przedstawSie())
