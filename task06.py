
from itertools import count, cycle

for el in count(int(input('Введите стартовое число: '))):
    if el <= 10:
        print(el)
    else:
        break

n = 1
my_list = [12, 43, 2, 66, 35]
for i in cycle(my_list):
    print(i)
    if n > 20:
        break
    n += 1



