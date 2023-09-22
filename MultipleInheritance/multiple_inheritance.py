class Runnable:
    def __init__(self, name):
        print("Hi, I'm "+name+" and i can run")


class Swimming:
    def __init__(self, name):
        print("Hi, I'm " + name + " and i can swim")


class Flight:
    def __init__(self, name):
        print("Hi, I'm " + name + " and i can flight")


class Person(Swimming, Runnable, Flight):
    def __init__(self, name):
        self.name = name
        print("Hi i'm "+name)
        Swimming.__init__(self, name)
        Runnable.__init__(self, name)
        Flight.__init__(self, name)


jack = Person("Jack")
print(help(Person))
