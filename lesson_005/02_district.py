# -*- coding: utf-8 -*-
from district.central_street.house1 import room1 as csh1r1
from district.central_street.house1 import room2 as csh1r2
from district.central_street.house2 import room1 as csh2r1
from district.central_street.house2 import room2 as csh2r2
from district.soviet_street.house1 import room1 as ssh1r1
from district.soviet_street.house1 import room2 as ssh1r2
from district.soviet_street.house2 import room1 as ssh2r1
from district.soviet_street.house2 import room2 as ssh2r2

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

csh1r1_p = csh1r1.folks
csh1r2_p = csh1r2.folks
csh2r1_p = csh2r1.folks
csh2r2_p = csh2r2.folks
ssh1r1_p = ssh1r1.folks
ssh1r2_p = ssh1r2.folks
ssh2r1_p = ssh2r1.folks
ssh2r2_p = ssh2r2.folks

spisok_centr = ",".join(csh1r1.folks+csh1r2.folks+csh2r1.folks+csh2r2.folks)
spispk_sovietskay = ",".join(ssh1r1.folks+ssh1r2.folks+ssh2r1.folks+ssh2r2.folks)

spisok_all = spisok_centr+spispk_sovietskay
print('На центральной улице живут:', spisok_centr)
print('На советчкой улице живут:', spispk_sovietskay)
print('На районе живут:', spisok_all)

