a = int(input("Введите сколько киллометров в первый день: "))
b = int(input("Введите вашу цель сколько киллометров нужно пробегать : "))
days = 1
while a < b:
    a = a + (a * 0.1)
    days += 1

print(f"Вы добьетесь поставленного результата через {days} дней")

