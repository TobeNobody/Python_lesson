my_list = []
n = int(input("Введите количество элементов в списке: "))
for i in range(n):
    my_list.append(input("Введите любые значения для заполнения списка: "))

print(my_list)

if n % 2 == 0:
    my_list[0::2], my_list[1::2] = my_list[1::2], my_list[0::2]
if n % 2 != 0:
    my_list[0:-1:2], my_list[1:-1:2] = my_list[1:-1:2], my_list[0:-1:2]

print(my_list)