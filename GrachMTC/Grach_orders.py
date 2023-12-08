import Grach_Bearish_Engulfing_Strategy as GR
import Grach_1_symbol as Ti


class Grach_order():
    # Заявки в quik
    def LimitLongEntry(self, quantity):
        """Новая Лимитная-Заявка для входа в ДЛИННУЮ позицию"""
        price = self+20  # Цена входа
        quan = quantity

        # Новая лимитная-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Ti.trader_index.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Ti.trader_index.account),  # Счет финам - 76008T3
            'ACTION': 'NEW_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Ti.trader_index.classCode),  # Код площадки
            'SECCODE': str(Ti.trader_index.secCode),  # Код тикера
            'OPERATION': 'B',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(quan),  # Кол-во в лотах
            'TYPE': 'L'}  # L = лимитная заявка (по умолчанию), M = рыночная заявка
        print(f'Новая лимитная заявка на вход в длинную позицию отправлена на рынок: {GR.qpProvider.SendTransaction(transaction)["data"]}\n')

    def LimitShortEntry(self, quantity):
        """Новая Лимитная-Заявка для входа в КОРОТКУЮ позицию"""
        price = self-20  # Цена входа
        quan = quantity

        # Новая лимитная-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Ti.trader_index.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Ti.trader_index.account),  # Счет финам - 76008T3
            'ACTION': 'NEW_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Ti.trader_index.classCode),  # Код площадки
            'SECCODE': str(Ti.trader_index.secCode),  # Код тикера
            'OPERATION': 'S',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(quan),  # Кол-во в лотах
            'TYPE': 'L'}  # L = лимитная заявка (по умолчанию), M = рыночная заявка
        print(f'Новая лимитная заявка на вход в короткую позицию отправлена на рынок: {GR.qpProvider.SendTransaction(transaction)["data"]}\n')

    def Long_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(self, quantity):
        """Новая Стоп-Заявка для ДЛИННОЙ позиции Тэйк-профит и стоп-лимит """
        price = self  # Цена входа
        quan = quantity

        # Новая стоп-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Ti.trader_index.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Ti.trader_index.account),  # Счет финам - 76008T3 r
            'ACTION': 'NEW_STOP_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Ti.trader_index.classCode),  # Код площадки
            'SECCODE': str(Ti.trader_index.secCode),  # Код тикера
            'OPERATION': 'S',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(quan),  # Кол-во в лотах
            'STOPPRICE': str(price + 25),  # ВОЗМОЖНО !!! активация тэйк-профита
            'STOP_ORDER_KIND': 'TAKE_PROFIT_AND_STOP_LIMIT_ORDER',  # Вид стоп-ордера : тэйк-профит и стоп-лимит
            'OFFSET': str(5),  # Величина отступа от максимума (минимума) цены последней сделки
            'OFFSET_UNITS': 'PRICE_UNITS',  # Единицы измерения отступа. PRICE_UNITS – в параметрах цены (шаг изменения равен шагу цены по данному инструменту).
            'SPREAD': str(3),  # Величина защитного спрэда.
            'SPREAD_UNITS': 'PRICE_UNITS',  # Единицы измерения защитного спрэда. PRICE_UNITS – в параметрах цены (шаг изменения равен шагу цены по данному инструменту).
            'MARKET_TAKE_PROFIT': 'NO',  # Признак исполнения заявки по рыночной цене при наступлении условия «тэйк-профит». Значения «YES» или «NO». Параметр заявок типа «Тэйк-профит и стоп-лимит»
            'STOPPRICE2': str(price - 50),  # ВОЗМОЖНО !!! стоп-лосс
            'IS_ACTIVE_IN_TIME': 'YES',  # Признак действия заявки типа «Тэйк-профит и стоп-лимит» в течение определенного интервала времени. Значения «YES» или «NO»
            'ACTIVE_FROM_TIME': str(100001),  # Время начала действия заявки типа «Тэйк-профит и стоп-лимит» в формате «ЧЧММСС»
            'ACTIVE_TO_TIME': str(235001),  # Время окончания действия заявки типа «Тэйк-профит и стоп-лимит» в формате «ЧЧММСС»
            'MARKET_STOP_LIMIT': 'NO', }
        print(f'Новая стоп-заявка для длинной позиции Тэйк-профит и стоп-лимит отправлена на рынок: {GR.qpProvider.SendTransaction(transaction)["data"]}\n')

    def Short_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(self, quantity):
        """Новая Стоп-Заявка для КОРОТКОЙ позиции Тэйк-профит и стоп-лимит """
        price = self  # Цена входа
        quan = quantity

        # Новая стоп-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Ti.trader_index.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Ti.trader_index.account),  # Счет финам - 76008T3
            'ACTION': 'NEW_STOP_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Ti.trader_index.classCode),  # Код площадки
            'SECCODE': str(Ti.trader_index.secCode),  # Код тикера
            'OPERATION': 'B',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(quan),  # Кол-во в лотах
            'STOPPRICE': str(price - 25),  # ВОЗМОЖНО !!! активация тэйк-профита
            'STOP_ORDER_KIND': 'TAKE_PROFIT_AND_STOP_LIMIT_ORDER',  # Вид стоп-ордера : тэйк-профит и стоп-лимит
            'OFFSET': str(5),  # Величина отступа от максимума (минимума) цены последней сделки
            'OFFSET_UNITS': 'PRICE_UNITS',  # Единицы измерения отступа. PRICE_UNITS – в параметрах цены (шаг изменения равен шагу цены по данному инструменту).
            'SPREAD': str(3),  # Величина защитного спрэда.
            'SPREAD_UNITS': 'PRICE_UNITS',  # Единицы измерения защитного спрэда. PRICE_UNITS – в параметрах цены (шаг изменения равен шагу цены по данному инструменту).
            'MARKET_TAKE_PROFIT': 'NO',  # Признак исполнения заявки по рыночной цене при наступлении условия «тэйк-профит». Значения «YES» или «NO». Параметр заявок типа «Тэйк-профит и стоп-лимит»
            'STOPPRICE2': str(price + 50),  # ВОЗМОЖНО !!! стоп-лосс
            'IS_ACTIVE_IN_TIME': 'YES',  # Признак действия заявки типа «Тэйк-профит и стоп-лимит» в течение определенного интервала времени. Значения «YES» или «NO»
            'ACTIVE_FROM_TIME': str(100001),  # Время начала действия заявки типа «Тэйк-профит и стоп-лимит» в формате «ЧЧММСС»
            'ACTIVE_TO_TIME': str(235001),  # Время окончания действия заявки типа «Тэйк-профит и стоп-лимит» в формате «ЧЧММСС»
            'MARKET_STOP_LIMIT': 'NO', }
        print(f'Новая стоп-заявка для короткой позиции Тэйк-профит и стоп-лимит отправлена на рынок: {GR.qpProvider.SendTransaction(transaction)["data"]}\n')

    def KILL_ALL_FUTURES_ORDERS_BUY(self):
        # Снятие всех заявок на ДЛИННУЮ позицию
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(1),  # Номер транзакции задается клиентом
            'ACCOUNT': str(Ti.trader_index.account),  # Счет финам - 76008T3
            'ACTION': 'KILL_ALL_FUTURES_ORDERS',  # Тип заявки: Снятие всех заявок на ДЛИННУЮ позицию
            'CLASSCODE': str(Ti.trader_index.classCode),  # Код площадки
            'SECCODE': str(Ti.trader_index.secCode),  # Код тикера
            'OPERATION': 'B',  # B = покупка, S = продажа
            'BASE_CONTRACT': "VTBR", }
        print(f'Снятие всех заявок на ДЛИННУЮ позицию отправлена на рынок: {GR.qpProvider.SendTransaction(transaction)["data"]}\n')

    def KILL_ALL_FUTURES_ORDERS_SELL(self):
        # Снятие всех заявок на КОРОТКУЮ позицию
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(1),  # Номер транзакции задается клиентом
            'ACCOUNT': str(Ti.trader_index.account),  # Счет финам - 76008T3
            'ACTION': 'KILL_ALL_FUTURES_ORDERS',  # Тип заявки: Снятие всех заявок на ДЛИННУЮ позицию
            'CLASSCODE': str(Ti.trader_index.classCode),  # Код площадки
            'SECCODE': str(Ti.trader_index.secCode),  # Код тикера
            'OPERATION': 'S',  # B = покупка, S = продажа
            'BASE_CONTRACT': "VTBR", }
        print(f'Снятие всех заявок на КОРОТКУЮ позицию отправлена на рынок: {GR.qpProvider.SendTransaction(transaction)["data"]}\n')
