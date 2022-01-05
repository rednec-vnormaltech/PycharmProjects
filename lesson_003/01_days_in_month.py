# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

def myee():
    user_input = input("Введите, пожалуйста, номер месяца: ")
    try:
        month = int(user_input)
    except:
        print('Не коректный ввод месяца!!!!!!!!!!')
    else:
        print('Вы ввели', month)
        if month == 1:
            print('31')
        elif month == 2:
            print('28')
        elif month == 3:
            print('31')
        elif month == 4:
            print('30')
        elif month == 5:
            print('31')
        elif month == 6:
            print('30')
        elif month == 7:
            print('31')
        elif month == 8:
            print('31')
        elif month == 9:
            print('30')
        elif month == 10:
            print('31')
        elif month == 11:
            print('30')
        elif month == 12:
            print('31')
        else:
            print('Не коректный ввод месяца')



user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if 0 < month < 13:
    if month in (1, 3, 5, 7, 8, 10, 12):
        print('в этом месяце', 31, 'день')
    elif month in (4, 6, 9, 11):
        print('в этом месяце', 30, 'дней')
    elif month == 2:
        print('в этом месяце', 28, 'дней')
else:
    print('Вы ввели некорректное число. Введите число от 1 до 12.')

