from QuikPy import QuikPy  # Работа с QUIK из Python через LUA скрипты QuikSharp


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    qpProvider = QuikPy()  # Вызываем конструктор QuikPy с подключением к локальному компьютеру с QUIK
    # qpProvider = QuikPy(Host='<Ваш IP адрес>')  # Вызываем конструктор QuikPy с подключением к удаленному компьютеру с QUIK

    #firmId = 'MC0063100000'  # Фирма
    #classCode = 'TQBR'  # Класс тикера
    #secCode = 'SBER'  # Тикер
    
    firmId = 'SPBFUT'  # Фирма
    classCode = 'SPBFUT'  # Класс тикера
    secCode = 'VBH3'  # Для фьючерсов: <Код тикера><Месяц экспирации: 3-H, 6-M, 9-U, 12-Z><Последняя цифра года>

    # Данные тикера
    securityInfo = qpProvider.GetSecurityInfo(classCode, secCode)["data"]  # Интерпретатор языка Lua, Таблица 4.21 Инструменты
    print(f'Информация о тикере {classCode}.{secCode} ({securityInfo["short_name"]}):')  # Короткое наименование инструмента
    print('Валюта:', securityInfo['face_unit'])  # Валюта номинала
    print('Кол-во десятичных знаков:', securityInfo['scale'])  # Точность (количество значащих цифр после запятой)
    print('Лот:', securityInfo['lot_size'])  # Размер лота
    print('Шаг цены:', securityInfo['min_price_step'])  # Минимальный шаг цены

    # Торговый счет тикера
    tradeAccount = qpProvider.GetTradeAccount(classCode)["data"]  # Торговый счет для класса тикера
    print(f'Торговый счет для тикера класса {classCode}: {tradeAccount}')

    # Последняя цена сделки
    lastPrice = float(qpProvider.GetParamEx(classCode, secCode, 'LAST')['data']['param_value'])  # Последняя цена сделки
    print('Последняя цена сделки:', lastPrice)

    # Выход
    qpProvider.CloseConnectionAndThread()  # Перед выходом закрываем соединение и поток QuikPy из любого экземпляра
