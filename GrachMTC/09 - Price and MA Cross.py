from datetime import datetime
import backtrader as bt


class PriceMACross(bt.Strategy):
    """Пересечение цены и SMA"""
    params = (  # Параметры торговой системы
        ('period_fast_sma', 8),  # Период SMA
        ('ADXPeriod', 14),  # Период ADX
        ('ADXLevelmin', 40),  # Уровень ADX
        ('ADXLevelmax', 35),  # Уровень ADX
    )

    def log(self, txt, dt=None):
        """Вывод строки с датой на консоль"""
        dt = bt.num2date(self.datas[0].datetime[0]) if dt is None else dt  # Заданная дата или дата текущего бара
        print(f'{dt.strftime("%d.%m.%Y %H:%M")}, {txt}')  # Выводим дату и время с заданным текстом на консоль

    def __init__(self):
        """Инициализация торговой системы"""
        self.close = self.data.close  # Цены закрытия
        self.order = None  # Заявка
        self.fast_sma = bt.indicators.SMA(self.data, period=self.p.period_fast_sma)  # SMA
        self.ADX = bt.indicators.AverageDirectionalMovementIndex(self.datas[0], period=self.p.ADXPeriod)
        self.PDI = bt.indicators.PlusDirectionalIndicator(self.datas[0], period=self.p.ADXPeriod)
        self.MDI = bt.indicators.MinusDirectionalIndicator(self.datas[0], period=self.p.ADXPeriod)
        self.crossup= bt.indicators.CrossUp(self.PDI,self.MDI)
        self.LOW = self.datas[0].low
        self.C = self.datas[0].close


        self.crossover = bt.indicators.CrossOver(self.ADX.DIplus, self.ADX.DIminus)  # инициализация пересечения fast_SMA и close

    def notify_order(self, order):
        """Изменение статуса заявки"""
        if order.status in [order.Submitted, order.Accepted]:  # Если заявка не исполнена (отправлена брокеру или принята брокером)
            return  # то статус заявки не изменился, выходим, дальше не продолжаем

        if order.status in [order.Completed]:  # Если заявка исполнена
            if order.isbuy():  # Заявка на покупку
                self.log(f'Bought @{order.executed.price:.2f}, Cost={order.executed.value:.2f}, Comm={order.executed.comm:.2f}')
            elif order.issell():  # Заявка на продажу
                self.log(f'Sold @{order.executed.price:.2f}, Cost={order.executed.value:.2f}, Comm={order.executed.comm:.2f}')
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:  # Заявка отменена, нет средств, отклонена брокером
            self.log('Canceled/Margin/Rejected')
        self.order = None  # Этой заявки больше нет

    def notify_trade(self, trade):
        """Изменение статуса позиции"""
        if not trade.isclosed:  # Если позиция не закрыта
            return  # то статус позиции не изменился, выходим, дальше не продолжаем

        self.log(f'Trade Profit, Gross={trade.pnl:.2f}, NET={trade.pnlcomm:.2f}')
    
    def next(self):
        """Получение следующего бара"""
        print(self.datas[0].low[-1])
        print(self.datas[0].low[0])
        self.log(f'Close={self.close[0]:.2f}')
        if self.order:  # Если есть неисполненная заявка
            return  # то выходим, дальше не продолжаем

        if not self.position:  # Если позиции нет
            if self.C[0] > self.C[-1]:# если цена пересекла fast_sma снизу вверх и свеча новая
                self.log('Buy Market')
                self.order = self.buy()  # Заявка на покупку по рыночной цене
        else:  # Если позиция есть
            if self.ADX[0] < self.ADX.DIplus[0]:
                self.log('Sell Market')
                self.order = self.sell()  # Заявка на продажу по рыночной цене


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    cerebro = bt.Cerebro()  # Инициируем "движок" BT
    cerebro.addstrategy(PriceMACross)  # Привязываем торговую систему с параметрами
    data = bt.feeds.GenericCSVData(
        # Можно принимать любые CSV файлы с разделителем десятичных знаков в виде точки https://backtrader.com/docu/datafeed-develop-csv/
        dataname='Data\\SPBFUT.VBH3_M1.txt',  # Файл для импорта
        separator='\t',  # Колонки разделены табуляцией
        dtformat='%d.%m.%Y %H:%M',  # Формат даты/времени DD.MM.YYYY HH:MI
        openinterest=-1,  # Открытого интереса в файле нет
        fromdate=datetime(2023, 2, 10),  # Начальная дата приема исторических данных (Входит)
        todate=datetime(2023, 2, 11))  # Конечная дата приема исторических данных (Не входит)
    cerebro.adddata(data)  # Привязываем исторические данные
    cerebro.broker.setcash(10000)  # Стартовый капитал для "бумажной" торговли
    cerebro.addsizer(bt.sizers.FixedSize, stake=1)  # Кол-во акций для покупки/продажи
    cerebro.broker.setcommission(commission=0.0005)  # Комиссия брокера 0.1% от суммы каждой исполненной заявки
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='TradeAnalyzer')  # Привязываем анализатор закрытых сделок
    brokerStartValue = cerebro.broker.getvalue()  # Стартовый капитал
    print(f'Старовый капитал: {brokerStartValue:.2f}')
    result = cerebro.run()  # Запуск торговой системы
    brokerFinalValue = cerebro.broker.getvalue()  # Конечный капитал
    print(f'Конечный капитал: {brokerFinalValue:.2f}')
    print(f'Прибыль/убытки с комиссией: {(brokerFinalValue - brokerStartValue):.2f}')
    analysis = result[0].analyzers.TradeAnalyzer.get_analysis()  # Получаем данные анализатора закрытых сделок
    print('Прибыль/убытки по закрытым сделкам:')
#    print(f'- Без комиссии {analysis["pnl"]["gross"]["total"]:.2f}')
  #  print(f'- С комиссией  {analysis["pnl"]["net"]["total"]:.2f}')
   # print(f'- Всего сделок  {analysis["total"]["total"]}')
    cerebro.plot(style='candlestick', barup='g', bardown='b',volume=False)  # Рисуем график. Требуется matplotlib версии 3.2.2 (pip install matplotlib==3.2.2)
