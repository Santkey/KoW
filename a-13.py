# rzucanie wyjątków (raise, assert)

def dzielenie(x, y):
    assert y != 0 "Y == 0"
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    print(x / y)

try:
    dzielenie(5, 0)
    print("Wszystko zaszło pomyslnie")

except ZeroDivisionError:
    print("Nastąpiło dzielenie przez zero")
    raise


