#!/usr/bin/env python3
# File     : 1093133.py
# Modified : <2020-3-11 Wed 00:57:26 gmt>
# URL      : https://ru.stackoverflow.com/questions/1093133/


from tabulate import tabulate


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {
            'quantity': 27,
            'price': 42,
        },
    ],
    '23456': [
        {
            'quantity': 22,
            'price': 510,
        },
        {
            'quantity': 32,
            'price': 520,
        },
    ],
    '34567': [
        {
            'quantity': 2,
            'price': 1200,
        },
        {
            'quantity': 1,
            'price': 1150,
        },
    ],
    '45678': [
        {
            'quantity': 50,
            'price': 100,
        },
        {
            'quantity': 12,
            'price': 95,
        },
        {
            'quantity': 43,
            'price': 97,
        },
    ],
}


def get_total(list):
    '''Выводит общее количество и суммарную стоимость продукта данной
    категории.'''
    t_qty = 0
    t_prc = 0
    for item in list:
        t_prc+=item['quantity'] * item['price']
        t_qty+=item['quantity']

    return t_qty, t_prc


def main():
    table = []
    for product, code in goods.items():
        quantity, price = get_total(store[code])
        table.append([product, quantity, price])

    print(tabulate(table, headers=['Товар', 'Количество (шт)', 'Oбщая стоимость'], tablefmt='psql'))


if __name__ == '__main__':
    main()

# End of  1093133.py