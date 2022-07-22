
my_list = [7, 6, 4, 2, 2, 1]
amount = int(input("Введите количество элементов, которые хотите ввести: "))
for el in range(amount):
    new_el = int(input("Введите новое значение в рейтинг: "))
    my_list.append(new_el)
    my_list.sort(reverse=True)
    print(my_list)

