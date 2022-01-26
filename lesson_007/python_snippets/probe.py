# Эмуляция операций и операторов python с помощью специальных методов

# Эмуляция операторов сравнения
#
# object.__eq__(self, other) - равенство двух объектов ==
# object.__ne__(self, other) - не равно !=
# object.__lt__(self, other) - строго меньше <
# object.__le__(self, other) - меньше или равно <=
# object.__gt__(self, other) - строго больше >
# object.__ge__(self, other) - больше или равно >=
#
# должны возвращать boolean - True/False

class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __eq__(self, other):
        return self.content == other.content


my_backpack = Backpack(gift='бутерброд')
son_backpack = Backpack(gift='бутерброд')

if my_backpack == son_backpack:
    print('Как мы похожи...')

if Backpack.__eq__(self=my_backpack, other=son_backpack):
    print('Как мы похожи...')
