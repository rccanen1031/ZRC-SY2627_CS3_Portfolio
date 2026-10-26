class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} eats food."

    def make_sound(self):
        return f"{self.name} makes a sound."


class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars fearlessly."

    def eat(self):
        return f"{self.name} eats meat."
    
    def feed(self):
        return self.eat()


class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} trumpets loudly."

    def eat(self):
        return f"{self.name} eats grass and fruits using its trunks."

    def feed(self):
        return self.eat()


class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} chatters annoyingly."

    def eat(self):
        return f"{self.name} eats bananas because he loves them."

    def feed(self):
        return self.eat()

# testing mic tes mic tes 

lion = Lion("Hillary")
elephant = Elephant("Clare")
monkey = Monkey("Jyohan")

print(lion.make_sound())
print(lion.eat())
print("-")

print(elephant.make_sound())
print(elephant.eat())
print("-")

print(monkey.make_sound())
print(monkey.eat())
print("")
