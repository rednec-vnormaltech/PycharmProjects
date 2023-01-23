import backtrader as bt
from datetime import datetime
import time  # Подписка на события по времени
from QuikPy import QuikPy  # Работа с Quik из Python через LUA скрипты QuikSharp

qpProvider = QuikPy()

"""Торговая система пересечения close и sma """
"""Long/Short - лимитные заявки"""
"""Выходы из Long/Short Лимитные заявки(по умолчанию) или Стоп-Заявка c Тэйк-профит и стоп-лимит"""

class Grach_SMA_Strategy(bt.Strategy):
    """- Отображает статус подключения- При приходе нового бара отображает его цены/объем- Отображает статус перехода к новым барам"""
    params = (  # Параметры торговой системы
        ('name', ''),  # Название торговой системы
        ('symbols', ''),  # Список торгуемых тикеров. По умолчанию торгуем все тикеры
        ('period_fast_sma', 13),  # Период SMA1
        ('period_slow_sma', 27),  # Период SMA2
    )

    account = '76008T3' # Финам
    classCode = 'SPBFUT'  # Код площадки
    secCode = 'VBH3'  # Код тикера
    TransId = 11772341  # Номер транзакции
    quantity = 1  # Кол-во в лотах

    counterPos = 0 # счетчик позиции 1 - в позиции купили; -1 - в позиции продали; 0 - нет позиции.  Возможно эта инфа храниться в self.position



    def log(self, txt, dt=None):
        """Вывод строки с датой на консоль"""
        dt = bt.num2date(self.datas[0].datetime[0]) if dt is None else dt  # Заданная дата или дата последнего бара первого тикера ТС
        print(f'{dt.strftime("%d.%m.%Y %H:%M")}, {txt}')  # Выводим дату и время с заданным текстом на консоль

        """Вывод строки с датой, sma  и больше меньше  на консоль"""
        print("\033[37m{}".format(""), int(self.datas[0].close[0] * 100000))
        if self.datas[0].close[0] > self.fast_sma[0]:
           print(f'********************************************************************************************** {int(self.datas[0].close[0] * 100000)} , {self.fast_sma[0]* 100000:.3f}, больше ')
        elif self.datas[0].close[0] < self.fast_sma[0]:
           print(f'********************************************************************************* {int(self.datas[0].close[0] * 100000)} , {self.fast_sma[0]* 100000:.3f}, меньше ')

    def __init__(self):
        """Инициализация торговой системы"""
        self.isLive = False  # Сначала будут приходить исторические данные

        self.fast_sma = bt.indicators.SMA(self.data, period=self.p.period_fast_sma)  # инициализация индикатора fast_SMA с параметрами
        self.slow_sma = bt.indicators.SMA(self.data, period=self.p.period_slow_sma)  # инициализация индикатора slow_SMA с параметрами

        self.crossover = bt.indicators.CrossOver(self.data, self.fast_sma)  # инициализация пересечения fast_SMA и close

    def next(self):
        """Приход нового бара тикера"""
        if self.p.name != '':  # Если указали название торговой системы, то будем ждать прихода всех баров
            lastdatetimes = [bt.num2date(data.datetime[0]) for data in self.datas]  # Дата и время последнего бара каждого тикера
            if lastdatetimes.count(lastdatetimes[0]) != len(lastdatetimes):  # Если дата и время последних баров не идентичны
                return  # то еще не пришли все новые бары. Ждем дальше, выходим
            print(self.p.name)
        for data in self.datas:  # Пробегаемся по всем запрошенным тикерам
            if self.p.symbols == '' or data._dataname in self.p.symbols:  # Если торгуем все тикеры или данный тикер
                self.log(f'{data._dataname} - {bt.TimeFrame.Names[data.p.timeframe]} {data.p.compression} - Open={data.open[0] * 100000:.2f}, High={data.high[0] * 100000:.2f}, Low={data.low[0] * 100000:.2f}, Close={data.close[0] * 100000:.2f}, Volume={data.volume[0] * 100:.0f}', bt.num2date(data.datetime[0]))

        """Выставление заявок в quik"""
        # Блок входа в Long
        if self.crossover > 0 and self.isLive == True:  # если цена пересекла fast_sma снизу вверх и свеча новая
            print("\033[32m{}".format("Сработало условие на покупку "), int(self.datas[0].close[0] * 100000))
            #KILL_ALL_FUTURES_ORDERS_BUY()
            #KILL_ALL_FUTURES_ORDERS_SELL()
            #LimitLongtEntry(int(self.datas[0].close[0] * 100000))   # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из КОРОТКОЙ позиции

            if not self.position:  # Если позиции нет
                print("self.position: ", self.position, " Покупка по цене", int(self.datas[0].close[0] * 100000), self.counterPos == 1)
                print(f'Текущий стакан {Grach_SMA_Strategy.classCode}.{Grach_SMA_Strategy.secCode}:', qpProvider.GetQuoteLevel2(Grach_SMA_Strategy.classCode, Grach_SMA_Strategy.secCode)['data']) # подписка на стакан
                #LimitLongEntry(int(self.datas[0].close[0] * 100000))

        # Блок входа в Short
        if self.crossover < 0 and self.isLive == True: # если цена пересекла fast_sma сверху вниз и свеча новая
            print("\033[34m{}".format("Сработало условие на продажу "), int(self.datas[0].close[0] * 100000))
            #KILL_ALL_FUTURES_ORDERS_SELL()
            #KILL_ALL_FUTURES_ORDERS_BUY()
            #LimitShortEntry(int(self.datas[0].close[0] * 100000)) # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из ДЛИННОЙ позиции


            if not self.position:  # Если позиции нет
                print("self.position: ", self.position, " Продажа по цене", int(self.datas[0].close[0] * 100000), self.counterPos == -1)
                #LimitShortEntry(int(self.datas[0].close[0] * 100000))

    def notify_data(self, data, status, *args, **kwargs):
        """Изменение статсуса приходящих баров"""
        dataStatus = data._getstatusname(status)  # Получаем статус (только при LiveBars=True)
        print(f'{data._dataname} - {dataStatus}')  # Статус приходит для каждого тикера отдельно
        self.isLive = dataStatus == 'LIVE'  # В Live режим переходим после перехода первого тикера


# ### Заявки в quik ###
def LimitLongEntry(n):
    """Новая Лимитная-Заявка для входа в ДЛИННУЮ позицию"""
    price = n  # Цена входа

    # Новая лимитная-заявка
    transaction = {  # Все значения должны передаваться в виде строк
        'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
        # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
        'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3 БКС - SPBFUTLS12r
        'ACTION': 'NEW_ORDER',  # Тип заявки: Новая заявка
        'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
        'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
        'OPERATION': 'B',  # B = покупка, S = продажа
        'PRICE': str(price),  # Цена исполнения
        'QUANTITY': str(Grach_SMA_Strategy.quantity),  # Кол-во в лотах
        'TYPE': 'L'}  # L = лимитная заявка (по умолчанию), M = рыночная заявка
    print(f'Новая лимитная заявка на вход в длинную позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}')

    #Long_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(n)  # После входа в длинную позицию выставляем стоп-заявку на Тэйк-профит и стоп-лимит


def LimitShortEntry(n):
    """Новая Лимитная-Заявка для входа в КОРОТКУЮ позицию"""
    price = n  # Цена входа

    # Новая лимитная-заявка
    transaction = {  # Все значения должны передаваться в виде строк
        'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
        # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
        'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3 БКС - SPBFUTLS12r
        'ACTION': 'NEW_ORDER',  # Тип заявки: Новая заявка
        'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
        'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
        'OPERATION': 'S',  # B = покупка, S = продажа
        'PRICE': str(price),  # Цена исполнения
        'QUANTITY': str(Grach_SMA_Strategy.quantity),  # Кол-во в лотах
        'TYPE': 'L'}  # L = лимитная заявка (по умолчанию), M = рыночная заявка
    print(f'Новая лимитная заявка на вход в короткую позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}')

    #Short_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(n) # После входа в короткую позицию выставляем стоп-заявку на Тэйк-профит и стоп-лимит


def Long_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(n):
    """Новая Стоп-Заявка для ДЛИННОЙ позиции Тэйк-профит и стоп-лимит """
    price = n  # Цена входа

    # Новая стоп-заявка
    transaction = {  # Все значения должны передаваться в виде строк
        'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
        # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
        'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3 БКС - SPBFUTLS12r
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
    print(f'Новая стоп-заявка для длинной позиции Тэйк-профит и стоп-лимит отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}')


def Short_TAKE_PROFIT_AND_STOP_LIMIT_ORDER(n):
    """Новая Стоп-Заявка для КОРОТКОЙ позиции Тэйк-профит и стоп-лимит """
    price = n  # Цена входа

    # Новая стоп-заявка
    transaction = {  # Все значения должны передаваться в виде строк
        'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
        # 'CLIENT_CODE': '',  # Код клиента. Для фьючерсов его нет
        'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3 БКС - SPBFUTLS12r
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
    print(f'Новая стоп-заявка для короткой позиции Тэйк-профит и стоп-лимит отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}')


def KILL_ALL_FUTURES_ORDERS_BUY():
    # Снятие всех заявок на ДЛИННУЮ позицию
    transaction = {  # Все значения должны передаваться в виде строк
        'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
        'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3 БКС - SPBFUTLS12r
        'ACTION': 'KILL_ALL_FUTURES_ORDERS',  # Тип заявки: Снятие всех заявок на ДЛИННУЮ позицию
        'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
        'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
        'OPERATION': 'B',  # B = покупка, S = продажа
        'BASE_CONTRACT': "RTKM", }
    print(f'Снятие всех заявок на ДЛИННУЮ позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}')


def KILL_ALL_FUTURES_ORDERS_SELL():
    # Снятие всех заявок на КОРОТКУЮ позицию
    transaction = {  # Все значения должны передаваться в виде строк
        'TRANS_ID': str(Grach_SMA_Strategy.TransId),  # Номер транзакции задается клиентом
        'ACCOUNT': str(Grach_SMA_Strategy.account),  # Счет финам - 76008T3 БКС - SPBFUTLS12r
        'ACTION': 'KILL_ALL_FUTURES_ORDERS',  # Тип заявки: Снятие всех заявок на ДЛИННУЮ позицию
        'CLASSCODE': str(Grach_SMA_Strategy.classCode),  # Код площадки
        'SECCODE': str(Grach_SMA_Strategy.secCode),  # Код тикера
        'OPERATION': 'S',  # B = покупка, S = продажа
        'BASE_CONTRACT': "RTKM", }
    print(f'Снятие всех заявок на КОРОТКУЮ позицию отправлена на рынок: {qpProvider.SendTransaction(transaction)["data"]}')