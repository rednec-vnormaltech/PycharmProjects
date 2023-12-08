from datetime import datetime
import backtrader as bt


class CloseSMA(bt.Strategy):
    params = (('period', 5),)

    def __init__(self):
        sma = bt.indicators.SMA(self.data, period=self.p.period)
        self.crossover = bt.indicators.CrossOver(self.data, sma)

    def next(self):
        if self.crossover > 0:
            self.buy(exectype=bt.Order.Limit, price=self.datas[0].close[0])
        elif self.crossover < 0:
            self.sell(exectype=bt.Order.Limit, price=self.datas[0].close[0])


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    cerebro = bt.Cerebro(stdstats=False)  # Инициируем "движок" BT, убираем стандартную статистику
    cerebro.addobserver(bt.observers.Broker)  # Берем стандартную кривую доходности
    cerebro.addobserver(bt.observers.DrawDown)  # Вместо сделок рисуем просадку
    cerebro.addobserver(bt.observers.BuySell, barplot=True, bardist=0.0001)  # Для небольшого временнОго интервала нужно уменьшить дистанцию от баров до маркеров входа/выхода
    cerebro.addstrategy(CloseSMA)  # Добавляем торговую систему
    data = bt.feeds.GenericCSVData(
        dataname='Data\\SPBFUT.SIH3_M60.txt',  # Файл для импорта
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
    cerebro.broker.setcommission(commission=0.0000001)  # Комиссия брокера 0.1% от суммы каждой исполненной заявки
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='TradeAnalyzer')  # Привязываем анализатор закрытых сделок
    brokerStartValue = cerebro.broker.getvalue()  # Стартовый капитал
    print(f'Старовый капитал: {brokerStartValue:.2f}')
    result = cerebro.run()  # Запуск торговой системы
    brokerFinalValue = cerebro.broker.getvalue()  # Конечный капитал
    print(f'Конечный капитал: {brokerFinalValue:.2f}')
    print(f'Прибыль/убытки с комиссией: {(brokerFinalValue - brokerStartValue):.2f}')
    analysis = result[0].analyzers.TradeAnalyzer.get_analysis()  # Получаем данные анализатора закрытых сделок
    print('Прибыль/убытки по закрытым сделкам:')
    print(f'                                    - Без комиссии {analysis["pnl"]["gross"]["total"]:.2f}')
    print(f'                                    - С комиссией  {analysis["pnl"]["net"]["total"]:.2f}')
    print(f'- Всего сделок  {analysis["total"]["total"]}')
    cerebro.plot(style='candlestick', barup='g', bardown='b')  # Рисуем график. Требуется matplotlib версии 3.2.2 (pip install matplotlib==3.2.2)
# ты гандон