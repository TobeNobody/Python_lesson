with open("file_task01.txt", "w+", encoding="utf-8") as f:
    line = input("Введите текст, оставив пробел в конце строки \n")
    while line:
        f.write(line)
        line = input("Введите текст, оставив пробел в конце строки \n")
        if not line:
            break

