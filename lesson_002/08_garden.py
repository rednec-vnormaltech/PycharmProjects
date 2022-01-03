#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set ={'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза'}
meadow_set ={'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка'}

print(type(garden_set))
print("Растут в саду",garden_set)
print(type(meadow_set))
print("Растут на лугу",meadow_set)


# выведите на консоль все виды цветов
# TODO здесь ваш код
print(garden_set.union(meadow_set))

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print(garden_set.intersection(meadow_set))

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
t_set =garden_set.intersection(meadow_set)
print(t_set)
print(garden_set.difference(t_set))

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
print(meadow_set.difference(t_set))


