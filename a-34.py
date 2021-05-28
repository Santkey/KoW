# wyrażenia regularne - powtórzenia

import re

if re.match("^[A-Z][a-z]*$","K"): # "*" pozwala na wystąpienie znaku wiele razy (ale nic musi być ani razu)
    print("Dopasowano!")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]+$","Ka"): # "+" pozwala na wystąpienie znaku wiele razy (ale musi wystąpić min 1 raz)
    print("Dopasowano!")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]?[A-Z]$","KaC"): # "?" dany znak może wystąpić we wzorze,ale nie musi
    print("Dopasowano!")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]{2,5}$","Kacper"): # "{}" dany znak musi wystąpić min. i max. {,5} brak limitu górnego {2,} brak limitu dolnego
    print("Dopasowano!")
else:
    print("Nie dopasowano")
