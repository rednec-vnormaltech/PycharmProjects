from datetime import datetime
from backtrader import Cerebro, TimeFrame
from wiseplat.BackTraderQuik import QKStore  # Хранилище QUIK
import Grach_SMA_Cross_Strategy as ts1
import Grach_Elder_Strategy as ts2
import Grach_Bearish_Engulfing_Strategy as ts3


"""Фундамент запуска Робота Запускается первым"""


# Эти параметры ипользуются только в заявках
class trader_index():
    account = '76008T3'  # Финам
    classCode = 'SPBFUT'  # Код площадки
    secCode = 'VBZ3'  # Код тикера
    TransId = 11772341  # Номер транзакции
    quantity = 1  # Кол-во в лотах


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    cerebro = Cerebro()  # Инициируем "движок" BackTrader

    # Один тикер, один временной интервал
    symbol = 'SPBFUT.VBZ3'
    store = QKStore()  # Хранилище QUIK (QUIK на локальном компьютере)
    #data = store.getdata(dataname=symbol, timeframe=TimeFrame.Days, fromdate=datetime(2018, 1, 1), LiveBars=False)  # Исторические дневные бары с заданной даты
    #data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, compression=1, LiveBars=False)  # Исторические минутные бары за все время
    data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, fromdate=datetime(2023, 9, 1, 8, 45), compression=60, name="m1", LiveBars=True)  # Исторические и новые минутные бары за все время
    cerebro.adddata(data)  # Добавляем данные

    data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, fromdate=datetime(2023, 9, 1, 8, 45), compression=60, name="m5", LiveBars=True)  # Исторические и новые минутные бары за все время
    cerebro.adddata(data)  # Добавляем данные

    data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, fromdate=datetime(2023, 9, 1, 9, 0), compression=240, name="m15", LiveBars=True)  # Исторические и новые минутные бары за все время
    cerebro.adddata(data)  # Добавляем данные

    #cerebro.addstrategy(ts1.Grach_SMA_Cross_Strategy)  # Добавляем торговую систему
    #cerebro.addstrategy(ts2.Grach_Elder_Strategy)  # Добавляем торговую систему
    cerebro.addstrategy(ts3.Grach_Bearish_Engulfing_Strategy)  # Добавляем торговую систему
    cerebro.run()  # Запуск торговой системы
    #cerebro.plot(style='candlestick', barup='g', bardown='b')  # Рисуем график. Требуется matplotlib версии 3.2.2 (pip install matplotlib==3.2.2)
