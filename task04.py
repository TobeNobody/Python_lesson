
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_task04', 'r', encoding="utf=8") as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])

with open('file_task04_new.txt', 'w', encoding="utf=8") as f_2:
    f_2.writelines(new_file)



