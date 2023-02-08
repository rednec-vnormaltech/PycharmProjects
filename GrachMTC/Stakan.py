import re
import Grach_SMA_Cross_Strategy
from QuikPy import QuikPy  # Работа с Quik из Python через LUA скрипты QuikSharp
from datetime import datetime



qpProvider = QuikPy()

classCode = 'SPBFUT'  # Код площадки
secCode = 'VBH3'  # Код тикера


def PrintCallback(data):
    """Пользовательский обработчик событий:
    - Изменение стакана котировок
    - Получение обезличенной сделки
    - Получение новой свечки
    """
    print(f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")} - {data["data"]}')  # Печатаем полученные данные

# работаем со стаканом получаем бид и аск
stakan_all = qpProvider.GetQuoteLevel2(classCode, secCode)['data'] # Получаем весь стакан
priceBuy_count = str(stakan_all["bid"]) # Строка содержит все предлоежения на покупку
priceSell_count = str(stakan_all["offer"]) # Строка содержит все предлоежения на ппродажу

qpProvider.OnQuote = PrintCallback


print(re.findall(r'\b\d+\b', priceBuy_count)[-2])# содержит лучший спрос из стакана
print(re.findall(r'\b\d+\b', priceSell_count)[0])# содержит лучшее предложение из стакана
