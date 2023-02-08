import backtrader as bt
from QuikPy import QuikPy  # Работа с Quik из Python через LUA скрипты QuikSharp

"""Торговая система пересечения close и sma ПЕРЕВОРОТНАЯ """
"""Long/Short - лимитные заявки"""
qpProvider = QuikPy()


def poison():  # Определяем есть ли позиция если есть то какая  1 buy  -1 sell
    futuresHoldings = qpProvider.GetFuturesHoldings()['data']  # Все фьючерсные позиции
    for p in futuresHoldings:  # пробегаемся по всему List[]
        if p['totalnet'] == 0:
            return 0
        if p['totalnet'] == 1:
            return 1
        if p['totalnet'] == -1:
            return -1
    if futuresHoldings == []:  # с начала дня при отсутсвие сделок приходит пустой LIST
        return 0


class Grach_SMA_Strategy(bt.Strategy):
    """- Отображает статус подключения- При приходе нового бара отображает его цены/объем- Отображает статус перехода к новым барам"""
    params = (  # Параметры торговой системы
        ('name', ''),  # Название торговой системы
        ('symbols', ''),  # Список торгуемых тикеров. По умолчанию торгуем все тикеры
        ('period_fast_sma', 3),  # Период SMA1
    )

    # Эти параметры ипользуются только в заявках
    account = '76008T3'  # Финам
    classCode = 'SPBFUT'  # Код площадки
    secCode = 'VBH3'  # Код тикера
    TransId = 11772341  # Номер транзакции
    quantity = 1  # Кол-во в лотах

    def log(self, txt, dt=None):
        """Вывод строки с датой на консоль"""
        dt = bt.num2date(self.datas[0].datetime[0]) if dt is None else dt  # Заданная дата или дата последнего бара первого тикера ТС
        print(f'{dt.strftime("%d.%m.%Y %H:%M")}, {txt}')  # Выводим дату и время с заданным текстом на консоль

    def __init__(self):
        """Инициализация торговой системы"""
        self.isLive = False  # Сначала будут приходить исторические данные

        self.fast_sma = bt.indicators.SMA(self.data, period=self.p.period_fast_sma)  # инициализация индикатора fast_SMA с параметрами

        self.crossover = bt.indicators.CrossOver(self.data, self.fast_sma)  # инициализация пересечения fast_SMA и close

    def next(self):
        """Приход нового бара тикера"""

        # При приходе каждой нового(живой свечи) удаляем все активные заявки
        if self.isLive:
            Grach_SMA_Strategy.KILL_ALL_FUTURES_ORDERS_BUY(self)
            Grach_SMA_Strategy.KILL_ALL_FUTURES_ORDERS_SELL(self)

        if self.p.name != '':  # Если указали название торговой системы, то будем ждать прихода всех баров
            lastdatetimes = [bt.num2date(data.datetime[0]) for data in self.datas]  # Дата и время последнего бара каждого тикера
            if lastdatetimes.count(lastdatetimes[0]) != len(lastdatetimes):  # Если дата и время последних баров не идентичны
                return  # то еще не пришли все новые бары. Ждем дальше, выходим
            print(self.p.name)
        for data in self.datas:  # Пробегаемся по всем запрошенным тикерам
            if self.p.symbols == '' or data._dataname in self.p.symbols:  # Если торгуем все тикеры или данный тикер
                self.log(f'{data._dataname} - {bt.TimeFrame.Names[data.p.timeframe]} {data.p.compression} - Open={data.open[0] * 100000:.2f}, High={data.high[0] * 100000:.2f}, Low={data.low[0] * 100000:.2f}, Close={data.close[0] * 100000:.2f}, Volume={data.volume[0] * 100:.0f}', bt.num2date(data.datetime[0]))

        """Выставление заявок в quik"""

        if poison() == 0:
            print("\nОткрытых позиций нет", poison())

            # Блок входа в Long
            if self.crossover > 0 and self.isLive == True:  # если цена пересекла fast_sma снизу вверх и свеча новая
                print("\033[32m{}".format("\nСработало условие на покупку "), int(self.datas[0].close[0] * 100000))

                Grach_SMA_Strategy.LimitLongEntry(int(self.datas[0].close[0] * 100000), 1)  # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из КОРОТКОЙ позиции

            # Блок входа в Short
            if self.crossover < 0 and self.isLive == True:  # если цена пересекла fast_sma сверху вниз и свеча новая
                print("\033[34m{}".format("\nСработало условие на продажу "), int(self.datas[0].close[0] * 100000))

                Grach_SMA_Strategy.LimitShortEntry(int(self.datas[0].close[0] * 100000), 1)  # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из ДЛИННОЙ позиции

        if poison() == 1:
            print("\nОткрыта позиция LONG", poison())

            # Блок выхода из Long
            if self.crossover < 0 and self.isLive == True:  # если цена пересекла fast_sma сверху вниз и свеча новая
                print("\033[34m{}".format("\nСработало условие на продажу "), int(self.datas[0].close[0] * 100000))

                Grach_SMA_Strategy.LimitShortEntry(int(self.datas[0].close[0] * 100000), 2)  # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из ДЛИННОЙ позиции

        if poison() == -1:
            print("\nОткрыта позиция SHORT", poison())

            # Блок выхода из Short
            if self.crossover > 0 and self.isLive == True:  # если цена пересекла fast_sma снизу вверх и свеча новая
                print("\033[32m{}".format("\nСработало условие на покупку "), int(self.datas[0].close[0] * 100000))

                Grach_SMA_Strategy.LimitLongEntry(int(self.datas[0].close[0] * 100000), 2)  # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из КОРОТКОЙ позиции

    def notify_data(self, data, status, *args, **kwargs):
        """Изменение статсуса приходящих баров"""
        dataStatus = data._getstatusname(status)  # Получаем статус (только при LiveBars=True)
        print(f'{data._dataname} - {dataStatus}')  # Статус приходит для каждого тикера отдельно
        self.isLive = dataStatus == 'LIVE'  # В Live режим переходим после перехода первого тикера

    # Заявки в quik
    def LimitLongEntry(self, quantity):
        """Новая Лимитная-Заявка для входа в ДЛИННУЮ позицию"""
        price = self  # Цена входа
        quan = quantity

        # Новая лимитная-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3
            'ACTION': 'NEW_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
            'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
            'OPERATION': 'B',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(quan),  # Кол-во в лотах
            'TYPE': 'L'}  # L = лимитная заявка (по умолчанию), M = рыночная заявка
        print(f'Новая лимитная заявка на вход в длинную позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}\n')

    def LimitShortEntry(self, quantity):
        """Новая Лимитная-Заявка для входа в КОРОТКУЮ позицию"""
        price = self  # Цена входа
        quan = quantity

        # Новая лимитная-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3
            'ACTION': 'NEW_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
            'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
            'OPERATION': 'S',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(quan),  # Кол-во в лотах
            'TYPE': 'L'}  # L = лимитная заявка (по умолчанию), M = рыночная заявка
        print(f'Новая лимитная заявка на вход в короткую позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}/n')

    def Long_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(self):
        """Новая Стоп-Заявка для ДЛИННОЙ позиции Тэйк-профит и стоп-лимит """
        price = self  # Цена входа

        # Новая стоп-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3 r
            'ACTION': 'NEW_STOP_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
            'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
            'OPERATION': 'S',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(Grach_SMA_Strategy.quantity),  # Кол-во в лотах
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
        print(f'Новая стоп-заявка для длинной позиции Тэйк-профит и стоп-лимит отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}\n')

    def Short_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(self):
        """Новая Стоп-Заявка для КОРОТКОЙ позиции Тэйк-профит и стоп-лимит """
        price = self  # Цена входа

        # Новая стоп-заявка
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
            # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
            'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3
            'ACTION': 'NEW_STOP_ORDER',  # Тип заявки: Новая заявка
            'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
            'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
            'OPERATION': 'B',  # B = покупка, S = продажа
            'PRICE': str(price),  # Цена исполнения
            'QUANTITY': str(Grach_SMA_Strategy.quantity),  # Кол-во в лотах
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
        print(f'Новая стоп-заявка для короткой позиции Тэйк-профит и стоп-лимит отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}\n')

    def KILL_ALL_FUTURES_ORDERS_BUY(self):
        # Снятие всех заявок на ДЛИННУЮ позицию
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(1),  # Номер транзакции задается клиентом
            'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3
            'ACTION': 'KILL_ALL_FUTURES_ORDERS',  # Тип заявки: Снятие всех заявок на ДЛИННУЮ позицию
            'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
            'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
            'OPERATION': 'B',  # B = покупка, S = продажа
            'BASE_CONTRACT': "VTBR", }
        print(f'Снятие всех заявок на ДЛИННУЮ позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}')

    def KILL_ALL_FUTURES_ORDERS_SELL(self):
        # Снятие всех заявок на КОРОТКУЮ позицию
        transaction = {  # Все значения должны передаваться в виде строк
            'TRANS_ID': str(1),  # Номер транзакции задается клиентом
            'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3
            'ACTION': 'KILL_ALL_FUTURES_ORDERS',  # Тип заявки: Снятие всех заявок на ДЛИННУЮ позицию
            'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
            'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
            'OPERATION': 'S',  # B = покупка, S = продажа
            'BASE_CONTRACT': "VTBR", }
        print(f'Снятие всех заявок на КОРОТКУЮ позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}\n')
