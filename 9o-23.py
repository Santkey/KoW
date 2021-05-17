#dekoratory

def decorator(func):
    def wrapper(): #opakowanie
        print("-------------")
        func()
        print("-------------")
    return wrapper

def hello():
    print("Hello World")

hello = decorator(hello)
hello()