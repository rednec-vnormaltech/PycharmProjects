from datetime import datetime
import backtrader as bt


class PriceChannelTrend(bt.Strategy):
    """Работа в канале и по тренду
    В канале переворачиваем позицию по противопоожным границам канала
    Если канал пробит по SL (от точки входа половина движения в противоположном направлении), то переходим в режим тренда
    В режиме тренда длинную позицию сопровождаем по нижней границе канала, короткую - по верхней
    При выходе из режима тренда переходим в режим тренд-канала, в основном, у самой цели для торговли в канале
    В режиме тренд-канала не ставим SL. После выхода переходим в режим канала
    """
    params = dict(
        Period=10)  # Период канала

    def __init__(self):
        self.highest = bt.ind.Highest(self.datas[0].high, period=self.p.Period)  # Highest High
        self.highest.plotinfo.subplot = False  # Отображаем на панели цен
        self.lowest = bt.ind.Lowest(self.datas[0].low, period=self.p.Period)  # Lowest Low
        self.lowest.plotinfo.subplot = False  # Отображаем на панели цен
        self.startOrder = None  # Начальная заявка
        self.primeOrder = None  # Мастер заявка TP, по которой отменяются OCO-заявка SL
        self.isTrendMode = False  # Режим тренда
        self.stopPrice = 0  # Цена SL

    def next(self):
        if not self.position:  # Если позиции нет (вход в первую позицию)
            if self.startOrder is not None:  # а заявки на вход есть
                self.cancel(self.startOrder)  # то снимаем заявки на вход
            self.startOrder = self.buy(exectype=bt.Order.Limit, price=self.lowest[0])  # Лимитная заявка на покупку по нижней границе канала
            self.sell(exectype=bt.Order.Limit, price=self.highest[0], oco=self.startOrder)  # Лимитная заявка на покупку по верхней границе канала
        else:  # Если позиция есть (первая и все последующие позиции)
            if self.primeOrder is None or self.primeOrder.status == self.primeOrder.Completed:  # Если заявки нет (первая позиция) или исполнился TP
                self.isTrendMode = False  # то переходим в режим канала
                if self.position.size > 0:  # Для длинной позиции
                    self.stopPrice = self.datas[0].close[0] - (self.highest[0] - self.datas[0].close[0]) / 8  # SL в 2 раза меньше TP
                    if self.stopPrice > self.lowest[0]:  # Если SL в канале
                        self.stopPrice = 0  # то SL не выставляем
                else:  # Для короткой позиции
                    self.stopPrice = self.datas[0].close[0] + (self.datas[0].close[0] - self.lowest[0]) / 8  # SL в 2 раза меньше TP
                    if self.stopPrice < self.highest[0]:  # Если SL в канале
                        self.stopPrice = 0  # то SL не выставляем
            elif self.primeOrder.alive():  # Если заявка есть и не исполнена
                self.cancel(self.primeOrder)  # то отменяем заявку
            elif self.primeOrder.status == self.primeOrder.Completed:  # Если исполнился TP
                self.isTrendMode = False  # то переходим в режим канала
            elif self.primeOrder.status == self.primeOrder.Canceled:  # Если исполнился SL (TP отменен)
                self.isTrendMode = True  # то переходим в режим тренда
            if self.position.size > 0:  # Длинная позиция
                if self.isTrendMode:  # В режиме тренда
                    self.primeOrder = self.sell(exectype=bt.Order.Stop, price=self.lowest[0])  # Сопровождаем по нижней границе канала (TS)
                else:  # В режиме канала
                    self.primeOrder = self.sell(exectype=bt.Order.Limit, price=self.highest[0])  # Сопровождаем по верхней границе канала (TP)
                    if self.stopPrice != 0:  # Если требуется установить SL
                        self.sell(exectype=bt.Order.Stop, price=self.stopPrice, oco=self.primeOrder)  # Переворотная стоп заявка на продажу (SL)
            else:  # Короткая позиция
                if self.isTrendMode:  # В режиме тренда
                    self.primeOrder = self.buy(exectype=bt.Order.Stop, price=self.highest[0])  # Сопровождаем по верхней границе канала (TS)
                else:  # В режиме канала
                    self.primeOrder = self.buy(exectype=bt.Order.Limit, price=self.lowest[0])  # Сопровождаем по нижней границе канала (TP)
                    if self.stopPrice != 0:  # Если требуется установить SL
                        self.buy(exectype=bt.Order.Stop, price=self.stopPrice, oco=self.primeOrder)  # Переворотная стоп заявка на покупку (SL)
            print(f'{bt.num2date(self.datas[0].datetime[0])} - {self.position.size} - {self.isTrendMode}')


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    cerebro = bt.Cerebro(stdstats=False)  # Инициируем "движок" BT, убираем стандартную статистику
    cerebro.addobserver(bt.observers.Broker)  # Берем стандартную кривую доходности
    cerebro.addobserver(bt.observers.DrawDown)  # Вместо сделок рисуем просадку
    cerebro.addobserver(bt.observers.BuySell, barplot=True, bardist=0.0001)  # Для небольшого временнОго интервала нужно уменьшить дистанцию от баров до маркеров входа/выхода
    cerebro.addstrategy(PriceChannelTrend)  # Добавляем торговую систему
    data = bt.feeds.GenericCSVData(
        dataname='Data\\SPBFUT.VBH3_M5.txt',  # Файл для импорта
        separator='\t',  # Колонки разделены табуляцией
        dtformat='%d.%m.%Y %H:%M',  # Формат даты/времени DD.MM.YYYY HH:MI
        openinterest=-1,  # Открытого интереса в файле нет
        timeframe=bt.TimeFrame.Minutes,  # Для временнОго интервала отличного от дневок нужно его указать
        compression=1,  # Для миннутного интервала, отличного от 1, его нужно указать
        fromdate=datetime(2022, 12, 16),  # Начальная дата приема исторических данных (Входит)
        todate=datetime(2023, 2, 11))  # Конечная дата приема исторических данных (Не входит)
    cerebro.adddata(data)  # Привязываем исторические данные
    cerebro.broker.setcash(10000)  # Стартовый капитал для "бумажной" торговли
    cerebro.broker.set_checksubmit(checksubmit=False)  # При перевороте позиции мы будем удваивать лот. Если в ТС будет больше лот, чем в позиции, то заявка отклонится по марже. Отключаем это правило
    cerebro.addsizer(bt.sizers.FixedReverser, stake=1)  # Кол-во в штуках для покупки/продажи для SAR
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
    print(f'- Без комиссии {analysis["pnl"]["gross"]["total"]:.2f}')
    print(f'- С комиссией  {analysis["pnl"]["net"]["total"]:.2f}')
    print(f'- Всего сделок  {analysis["total"]["total"]}')
    cerebro.plot(style='candlestick', barup='g', bardown='b')  # Рисуем график. Требуется matplotlib версии 3.2.2 (pip install matplotlib==3.2.2)
