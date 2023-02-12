from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def __str__(self):
        return "{} : {} money, {} food, {} dirt".format(__class__.__name__, self.money, self.food, self.dirt)


class Man(House):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def act(self):
        self.fullness -= 10

        if self.fullness < 0:
            cprint("Man Die :(", color='red')

        if self.happiness < 10:
            cprint("Man die at depresion!", color='red')

    def eat(self, quantity):
        if self.food >= quantity and quantity <= 30:
            self.food -= quantity
        else:
            cprint("Food finish!", color='red')

    def __str__(self):
        res = super(Man, self).__str__()
        return res + "\n{} : {} {} fullness {} happiness".format(__class__.__name__,self.name, self.fullness,
                                                                 self.happiness)


class Husband(Man):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super(Husband, self).act()
        if self.money <= 10:
            self.work()
        if self.fullness < 5:
            self.eat(randint(1, 50))
        if self.happiness < 15:
            self.gaming()

    def eat(self, quantity):
        super(Husband, self).eat(quantity=quantity)

    def work(self):
        self.money += 150

    def gaming(self):
        self.happiness += 20


class Wife(Man):

    coat_points = 0

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super(Wife, self).act()
        if self.food < 5:
            self.shopping(randint(10, 100))
        if self.dirt > 40:
            self.clean_house()
        if self.happiness < 15:
            self.buy_fur_coat()

    def eat(self, quantity):
        super(Wife, self).eat(quantity=quantity)

    def shopping(self, quantity):
        self.food += quantity
        self.money -= quantity

    def buy_fur_coat(self):
        self.money -= 350
        self.happiness += 60
        self.coat_points += 1

    def clean_house(self):
        if 0 < self.dirt <= 100:
            self.dirt = 0
        else:
            cprint("Please leave the house", color="red")


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirt += 5
    serge.act()
    masha.act()
    if home.dirt >= 90:
        serge.happiness -= 10
        masha.happiness -= 10
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

cprint("Shuba", masha.coat_points)
cprint("Money", home.money)
cprint("Food", home.food)
