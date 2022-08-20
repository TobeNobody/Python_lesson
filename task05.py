
with open('file_task05.txt', 'w+', encoding="utf-8") as f:
    try:
        line = input('Введите цифры через пробел: ')
        f.writelines(line)
        my_numb = line.split()
        print(sum(map(int, my_numb)))
    except ValueError:
        print('Вы должны ввести цифры')
