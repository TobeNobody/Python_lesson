from sys import argv

def salary():
    try:
        a, b, c = map(int, argv[1:])
        print(f"Заработная плата сотрудника составляет  {a * b + c} рублей")
    except ValueError:
        print("Вы ввели не число")

salary()

