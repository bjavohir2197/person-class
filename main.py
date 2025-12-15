class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Mening ismim {self.name}, men {self.age} yoshdaman."

p1 = Person("Ali", 20)
print(p1.introduce())
