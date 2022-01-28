from random import choice


class SomeClass:
    x = 85

    def __init__(self):
        self.x = 178

    def method_one(self):
        x = 23
        print('method_one', self.x)

    def method_two(self):
        x = 34
        def func_one():
             # x = 56
            print('func_one', SomeClass.x)

        func_one()
        print('method_two', x)


x = 12
obj = SomeClass()
obj.method_one()
obj.method_two()
print('global', x)
