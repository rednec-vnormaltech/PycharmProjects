from random import randint
from termcolor import cprint

_secret_number = []
bulls = 0
cow = 0


def riddle_number():
    """Функция загадывает случайное число"""

    global _secret_number
    _secret_number = randint(1, 1000)
    cprint('Загаданное число {}'.format(_secret_number), 'cyan')


def check_number(number_players, user_number):
    """Проверяет число введенное пользователем и
        возвращает словарь {'bulls': N, 'cows': N}
        НО СНАЧАЛА СДЕЛАЕМ ФУНКЦИЮ СПИСКОМ
    """
    global bulls
    global cow

    dict_players = list(str(number_players))
    x = int(dict_players[0])
    y = int(dict_players[1])
    z = int(dict_players[2])

    dict_secret_number = list(str(_secret_number))
    x1 = int(dict_secret_number[0])
    y1 = int(dict_secret_number[1])
    z1 = int(dict_secret_number[2])

    if x == x1:
        bulls += 1
    if y == y1:
        bulls += 1
    if z == z1:
        bulls += 1

    if x == y1:
        cow += 1
    if y == z1:
        cow += 1
    if z == x1:
        cow += 1

    if x == z1:
        cow += 1
    if y == x1:
        cow += 1
    if z == y1:
        cow += 1

    print(x, y, z)
    print(x1, y1, z1)

    print('быков:', bulls, ', коров:', cow)

    return bulls, cow


def endgames(user_number):
    cprint('Выйграл игрок номер {}'.format(user_number), color='red')
