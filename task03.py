
with open("file_task03", "r", encoding="utf-8") as f:
    lst_all = []
    lst = []
    line = f.readlines()
    for value in line:
        salary = value.split()
        all_sal = salary[1]
        lst_all.append(all_sal)
        if int(salary[1]) < 20000:
            losers = salary[0][:-1]
            lst.append(losers)

    print(f"Список работников с окладом меньше 20000 - {lst}")
    print(f"Средняя величина доходов сотрудников - {sum(map(int, lst_all)) / len(lst_all)}")
