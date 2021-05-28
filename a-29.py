#hermetyzacja - ukrywanie danych

class Test:
    __lista = []  #można użyc podekreślenia do prywatyzacji zmiennych wewnątrz klasy
    def dodaj(self, arg):
        self.__lista.append(arg)
    
    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._Test__lista.append("X") #hermetyzajca w python nie istnieje 

print(obj.zdejmij())
print(obj._Test__lista)
