#skrócony operator if, inne zastosowanie else

#print("Prawda") if 5 > 2 else print("fałsz")

a = "Parzysta" if 10 % 2 == 0 else "nieparzysta" #mozna zwracać wartości string i int
print(a)

for i in range(10):
    if i > 5:
        continue
else:
    print()

try:
    a = 5/0

except ZeroDivisionError:
    print("Dzielenie przez zero")

else:
    print("Koniec")

finally:
    print("Zawsze")

