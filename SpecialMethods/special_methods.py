class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __add__(self, other):
        return self.age + other.age

    def __len__(self):
        return self.age

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __del__(self):
        print("The person object is destroyed!")


jack = Person("Jack", "Lomonosov", 45)
jane = Person("Jane", "Sparrow", 30)

print(jane + jack)
print(len(jane))
print(jack)
