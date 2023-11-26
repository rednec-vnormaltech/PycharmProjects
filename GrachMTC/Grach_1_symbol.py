from datetime import datetime
from backtrader import Cerebro, TimeFrame
from wiseplat.BackTraderQuik import QKStore  # Хранилище QUIK
import Grach_SMA_Cross_Strategy as ts1
import Grach_Elder_Strategy as ts2


"""Фундамент запуска Робота Запускается первым"""


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    cerebro = Cerebro()  # Инициируем "движок" BackTrader

    # Один тикер, один временной интервал
    symbol = 'SPBFUT.VBZ3'
    store = QKStore()  # Хранилище QUIK (QUIK на локальном компьютере)
    #data = store.getdata(dataname=symbol, timeframe=TimeFrame.Days, fromdate=datetime(2018, 1, 1), LiveBars=False)  # Исторические дневные бары с заданной даты
    #data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, compression=1, LiveBars=False)  # Исторические минутные бары за все время
    data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, fromdate=datetime(2023, 11, 22, 17, 0), compression=1, name="m1", LiveBars=True)  # Исторические и новые минутные бары за все время
    cerebro.adddata(data)  # Добавляем данные

    data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, fromdate=datetime(2023, 11, 22, 17, 0), compression=5, name="m5", LiveBars=True)  # Исторические и новые минутные бары за все время
    cerebro.adddata(data)  # Добавляем данные

    data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, fromdate=datetime(2023, 11, 22, 17, 0), compression=15, name="m15", LiveBars=True)  # Исторические и новые минутные бары за все время
    cerebro.adddata(data)  # Добавляем данные

    #cerebro.addstrategy(ts1.Grach_SMA_Cross_Strategy)  # Добавляем торговую систему
    cerebro.addstrategy(ts2.Grach_Elder_Strategy)  # Добавляем торговую систему
    cerebro.run()  # Запуск торговой системы
    #cerebro.plot(style='candlestick', barup='g', bardown='b')  # Рисуем график. Требуется matplotlib версии 3.2.2 (pip install matplotlib==3.2.2)
