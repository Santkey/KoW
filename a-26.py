# klasy i dziedziczenie

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def getVoice(self):
        print("How How")

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow")

class Wolf(Dog):
    def getVoice(self):
        print("Awooooo,")
        super().getVoice()

dog = Dog("Burek", 10)
print(dog.name)
print(dog.age)
dog.getVoice()

cat = Cat("Mruczek", 5)
print(cat.name)
print(cat.age)
cat.getVoice()

wolf = Wolf("Kieł", 15)
print(wolf.name)
print(wolf.age)
wolf.getVoice()


