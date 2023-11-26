import pandas as pd

# читаем файл с разделителем пробел
df = pd.read_csv('SPBFUT.RIH3_D1.txt', delimiter='\t')

# выбираем столбец по его названию и записываем в другой файл
df['close'].to_csv('new_file.txt', sep='\t', index=False)