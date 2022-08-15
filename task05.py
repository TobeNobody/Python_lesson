
from functools import reduce

lst = [el for el in range(99, 1001) if el % 2 == 0]
print(lst)
print(reduce(lambda a, b: a * b, lst))


