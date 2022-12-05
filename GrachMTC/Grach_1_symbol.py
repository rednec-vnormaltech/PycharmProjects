from datetime import datetime
from backtrader import Cerebro, TimeFrame
from BackTraderQuik.QKStore import QKStore  # Хранилище QUIK
import Grach_SMA_Strategy as tss


"""Стратегия для торговли 1 символом и 1 контрактом"""


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    cerebro = Cerebro()  # Инициируем "движок" BackTrader

    # Один тикер, один временной интервал
    symbol = 'SPBFUT.VBZ2'
    store = QKStore()  # Хранилище QUIK (QUIK на локальном компьютере)
    #data = store.getdata(dataname=symbol, timeframe=TimeFrame.Days, fromdate=datetime(2018, 1, 1), LiveBars=False)  # Исторические дневные бары с заданной даты
    #data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, compression=1, LiveBars=False)  # Исторические минутные бары за все время
    data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, fromdate=datetime(2022, 10, 15, 7, 0), compression=1, LiveBars=True)  # Исторические и новые минутные бары за все время
    cerebro.adddata(data)  # Добавляем данные
    cerebro.addstrategy(tss.Grach_SMA_Strategy)  # Добавляем торговую систему
    cerebro.run()  # Запуск торговой системы
    cerebro.plot(style='candlestick', barup='g', bardown='b')  # Рисуем график. Требуется matplotlib версии 3.2.2 (pip install matplotlib==3.2.2)
