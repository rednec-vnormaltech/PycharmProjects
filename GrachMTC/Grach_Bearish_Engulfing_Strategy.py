import backtrader as bt
from QuikPy import QuikPy  # Работа с Quik из Python через LUA скрипты QuikSharp
import pandas as pd
import Grach_orders as Gr_ord
import Grach_1_symbol as Ti


"""Торговая система Бычье/Медвежье поглащение """
"""1) При появление Медвежьего поглащения следующую свечу торгуем вниз """
"""2) При появление Бычьего поглащения следующую свечу торгуем вверх """

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


class Grach_Bearish_Engulfing_Strategy(bt.Strategy):
    """- Отображает статус подключения- При приходе нового бара отображает его цены/объем- Отображает статус перехода к новым барам"""
    params = (  # Параметры торговой системы
        ('name', ''),  # Название торговой системы
        ('symbols', ''),  # Список торгуемых тикеров. По умолчанию торгуем все тикеры
        ('period_fast_sma', 3),  # Период SMA1
    )

    def log(self, txt, dt=None):
        """Вывод строки с датой на консоль"""
        dt = bt.num2date(self.datas[0].datetime[0]) if dt is None else dt  # Заданная дата или дата последнего бара первого тикера ТС
        print(f'{dt.strftime("%d.%m.%Y %H:%M")}, {txt}')  # Выводим дату и время с заданным текстом на консоль

    def __init__(self):
        """Инициализация торговой системы"""

        self.fast_sma15 = bt.indicators.SMA(self.data2, period=self.p.period_fast_sma)  # инициализация индикатора fast_SMA с параметрами 15-минутки
        self.crossover15 = bt.indicators.CrossOver(self.data2, self.fast_sma15)  # инициализация пересечения fast_SMA и close 15-минутки
        self.isLive = False  # Сначала будут приходить исторические данные
        self.df = pd.DataFrame(columns=['Дата', 'Инструмент', 'Тип Сделки', 'Цена', 'Прибыль'])
        self.testtr = 0


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
        # Блок выхода из Long
        if self.testtr == 1:
            if poison() == 0:  # Если открыта позиция BUY
                print("\nОткрыта позиция LONG", poison())
                if self.datas[0].open[0] > self.datas[0].close[0] and self.isLive == False:  # если цена пересекла fast_sma сверху вниз и свеча новая
                    print("\033[34m{}".format("\nСработало условие на выход из Длинной позиции "), int(self.datas[0].close[0] * 100000))
                    # Gr_ord.Grach_order.LimitShortEntry(int(self.datas[0].close[0] * 100000), Ti.trader_index.quantity)  # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из ДЛИННОЙ позиции
                    """Тестирование"""
                    new_data_row = {
                        'Дата': [bt.num2date(self.data.datetime[0])],  # Замените new_datetime на вашу новую дату
                        'Инструмент': [Ti.trader_index.secCode],  # Замените new_datetime на вашу новую дату
                        'Тип Сделки': ['Закрытие покупки'],  # Замените на ваш новый тип сделки
                        'Цена': [self.datas[0].close[0] * 100000],  # Замените на вашу новую цену
                        'Прибыль': [self.datas[0].close[0] * 100000 - self.df['Цена'].iloc[-1] if not self.df.empty else 0],
                    }
                    # Создаем DataFrame для новой строки данных
                    new_df_row = pd.DataFrame(new_data_row, index=[0])
                    # Используем метод concat для добавления новой строки к существующему DataFrame self.df
                    self.df = pd.concat([self.df, new_df_row], ignore_index=True)
                    # Записываем DataFrame в Excel при необходимости
                    self.df.to_excel('./teams.xlsx')
                    self.testtr = 0

        # Блок выхода из Short
        if self.testtr == -1:
            if self.datas[1].open[0] < self.datas[1].close[0] and self.isLive == False:
                print("\033[32m{}".format("\nСработало условие на выход из Короткой позиции "), int(self.datas[1].close[0] * 100000))
                # Gr_ord.Grach_order.LimitLongEntry(int(self.datas[0].close[0] * 100000), Ti.trader_index.quantity)  # При CROSS торговле с Тэйк-профит и стоп-лимит исполняет выход из КОРОТКОЙ позиции
                print("\033[0m{}".format("\n"))  # Возвращает цвет текста опять на белый
                """Тестирование"""
                new_data_row = {
                    'Дата': [bt.num2date(self.data.datetime[0])],  # Замените new_datetime на вашу новую дату
                    'Инструмент': [Ti.trader_index.secCode],  # Замените new_datetime на вашу новую дату
                    'Тип Сделки': ['Закрытие продажи'],  # Замените на ваш новый тип сделки
                    'Цена': [self.datas[1].close[0] * 100000],  # Замените на вашу новую цену
                    'Прибыль': [(self.datas[1].close[0] * 100000 - self.df['Цена'].iloc[-1]) * -1 if not self.df.empty else 0],
                }
                # Создаем DataFrame для новой строки данных
                new_df_row = pd.DataFrame(new_data_row, index=[0])
                # Используем метод concat для добавления новой строки к существующему DataFrame self.df
                self.df = pd.concat([self.df, new_df_row], ignore_index=True)
                # Записываем DataFrame в Excel при необходимости
                self.df.to_excel('./teams.xlsx')
                self.testtr = 0


        # Блок входа в Long
        if self.testtr ==0:
            if poison() == 0 and self.isLive == False: # Если открытых позиций НЕТ
                print("\nОткрытых позиций нет", poison())
                #Бычье поглащение
                # Вычисление размера тела предыдущей свечи
                body_size_prev = self.datas[1].open[-1] - self.datas[1].close[-1]
                # Вычисление размера тела текущей свечи
                body_size_current = self.datas[1].close[0] - self.datas[1].open[0]
                # Если предыдущая свеча была низходящей и текущая свеча бычья поглощает предыдущую
                if body_size_prev > 0 and body_size_current > 0 and self.datas[1].open[0] <= self.datas[1].close[-1] and self.data2.close[0] > self.fast_sma15[0]:
                    # Ваш код для входа в длиную позицию
                    print("\033[32m{}".format("\nСработало условие на покупку (Бычье поглощение):"), int(self.datas[1].close[0] * 100000)) # Выводит текст зеленым цветом
                    print("\033[0m{}".format("\n")) # Возвращает цвет текста опять на белый
                    #Gr_ord.Grach_order.LimitLongEntry(int(self.datas[0].close[0] * 100000), Ti.trader_index.quantity)  # Новая Лимитная-Заявка для входа в ДЛИННУЮ позицию
                    """Тестирование"""
                    new_data_row = {
                        'Дата': [bt.num2date(self.data.datetime[0])],  # Замените new_datetime на вашу новую дату
                        'Инструмент': [Ti.trader_index.secCode],  # Замените new_datetime на вашу новую дату
                        'Тип Сделки': ['Покупка'],  # Замените на ваш новый тип сделки
                        'Цена': [self.datas[1].close[0] * 100000],  # Замените на вашу новую це
                    }
                    # Создаем DataFrame для новой строки данных
                    new_df_row = pd.DataFrame(new_data_row, index=[0])
                    # Используем метод concat для добавления новой строки к существующему DataFrame self.df
                    self.df = pd.concat([self.df, new_df_row], ignore_index=True)
                    # Записываем DataFrame в Excel при необходимости
                    self.df.to_excel('./teams.xlsx')
                    self.testtr =1



        # Блок входа в Short
        if self.testtr == 0:
            if poison() == 0 and self.isLive == False: # Если открытых позиций НЕТ
                print("\nОткрытых позиций нет", poison())
                # Медвежье поглащение
                # Вычисление размера тела предыдущей свечи
                body_size_prev = self.datas[1].close[-1] - self.datas[1].open[-1]
                # Вычисление размера тела текущей свечи
                body_size_current = self.datas[1].open[0] - self.datas[1].close[0]
                # Если предыдущая свеча была восходящей и текущая свеча медвежья поглощает предыдущую
                if body_size_prev > 0 and body_size_current > 0 and self.datas[1].open[0] >= self.datas[1].close[-1] and self.data2.close[0] < self.fast_sma15[0]:
                    # Ваш код для входа в длиную позицию
                    print("\033[34m{}".format("\nСработало условие на продажу: "), int(self.datas[1].close[0] * 100000)) # Выводит текст синим цветом
                    print("\033[0m{}".format("\n")) # Возвращает цвет текста опять на белый
                    #Gr_ord.Grach_order.LimitShortEntry(int(self.datas[0].close[0] * 100000), Ti.trader_index.quantity)  # Новая Лимитная-Заявка для входа в КОРОТКУЮ позицию
                    """Тестирование"""
                    new_data_row = {
                        'Дата': [bt.num2date(self.data.datetime[0])],  # Замените new_datetime на вашу новую дату
                        'Инструмент': [Ti.trader_index.secCode],  # Замените new_datetime на вашу новую дату
                        'Тип Сделки': ['Продажа'],  # Замените на ваш новый тип сделки
                        'Цена': [self.datas[1].close[0] * 100000],  # Замените на вашу новую цену
                    }
                    # Создаем DataFrame для новой строки данных
                    new_df_row = pd.DataFrame(new_data_row, index=[0])
                    # Используем метод concat для добавления новой строки к существующему DataFrame self.df
                    self.df = pd.concat([self.df, new_df_row], ignore_index=True)
                    # Записываем DataFrame в Excel при необходимости
                    self.df.to_excel('./teams.xlsx')
                    self.testtr = -1



    def notify_data(self, data, status, *args, **kwargs):
        """Изменение статсуса приходящих баров"""
        dataStatus = data._getstatusname(status)  # Получаем статус (только при LiveBars=True)
        print(f'{data._dataname} - {dataStatus}')  # Статус приходит для каждого тикера отдельно
        self.isLive = dataStatus == 'LIVE'  # В Live режим переходим после перехода первого тикера



