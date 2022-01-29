from termcolor import cprint
import random as r


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 100
        self.food = 100
        self.money = 100

    def __str__(self):
        return 'Я - {}, сытость {}, Еда {}, Деньги {} '.format(self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            cprint('{} поел '.format(self.name), color='green')
            self.fullness += 30
            self.food -= 10
        else:
            cprint('У {} нет еды '.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу '.format(self.name), color='blue')
        self.money += 50
        self.fullness -= 20

    def shopping(self):
        cprint('{} сходил в магазин,  '.format(self.name), color='cyan')
        self.money -= 50
        self.food += 20

    def act(self):

        dice = r.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1 or dice == 6:
            self.work()
        elif dice == 2 or dice == 4:
            self.eat()
        elif dice == 3 or dice == 5:
            self.shopping()


vasya = Man(name="Василий")

for day in range(1, 500):
    print('\n================== день {} =================='.format(day))
    print(vasya)
    vasya.act()
    if vasya.fullness <= 0:
        cprint('{} умер...'.format(vasya.name), color='red')
        break
