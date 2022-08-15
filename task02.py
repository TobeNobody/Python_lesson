
lst = [17, 5, 13, 24, 5, 65, 1, 17, 18, 18, 124, 5]
my_lst = [el for i, el in enumerate(lst) if i > 0 and lst[i] > lst[i - 1]]
print(lst)
print(my_lst)
print(list(enumerate(lst)))


