
with open("fail_task02", "r", encoding="utf-8") as f:
    line = f.readlines()
    print(f"Количество строк {len(line)}")
    for index, value in enumerate(line, 1):
        print(index, value, end="")
        new_line = len(value.split())
        print(f"Количество слов в {index} строке - {new_line}")