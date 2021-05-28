# wyrażenie regularne - klasy znaków, przedziały

import re
# jeżeli wzór ma się rozpoczynać od danego znaku to piszemy ^, a jeżeli kończyć to ¢
# zbiór znaków w nawiasach kwadratowych oznacza grupę
# A-Z oznacza zbiór znaków alfabetu od a do z w ascii
# zapisywany poza klasą znaku neguje zbiór



if re.match("^[rR]ok[-_=][0-9][0-9][0-9][0-9]$", "Rok_2020"): # "." jest wartością uznawana za jakąkolwiek
    print("dopasowano")
else:
    print("nie dopasowano")