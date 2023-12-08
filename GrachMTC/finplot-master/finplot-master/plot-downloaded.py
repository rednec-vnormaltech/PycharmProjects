# plot-downloaded.py
import pandas as pd
import finplot as fplt

# Загрузка данных из CSV-файла
df = pd.read_csv('cache.csv')
df['Date'] = pd.to_datetime(df['Date'])  # Преобразование столбца Date в формат datetime
df = df.set_index('Date')  # Установка столбца Date в качестве индекса

# Построение свечного графика на основе данных об открытии, закрытии, максимальной и минимальной ценах
fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
fplt.show()  # Отображение графика
