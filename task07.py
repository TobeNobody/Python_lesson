import statistics
import json

with open("file_task07.txt", "r", encoding="utf=8") as f:
    line = f.readlines()
    lst = []
    for i in line:
        profit = int(i.split()[2]) - int(i.split()[3])
        print(f"Прибыль компании {i.split()[0]} равна - {profit}")
        if profit > 0:
            lst.append(profit)
    average_profit = statistics.fmean(map(int, lst))
    print(f"Средняя прибыль равна - {average_profit}")

    result = [{i.split()[0]: (int(i.split()[2]) - int(i.split()[3])) for i in line}, {"average_profit": average_profit}]
    print(result)

with open("eprst07.json", "w", encoding="utf=8") as f_json:
    json.dump(result, f_json)
