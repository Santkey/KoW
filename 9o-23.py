#dekoratory

def decorator(func): #zdefiniowanie funkcji dekorator dla funkcji (func)
    def wrapper(): #definicja opakowania
        print("opakowanie")
        func()
        print("opakowanie")
    return wrapper

def hello():
    print("Hello World")

hello = decorator(hello)
hello()

@decorator
def witaj():
    print("Witaj Świecie")

witaj()