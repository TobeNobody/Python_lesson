a = 5
print(a)

b = input('Введите любые символы: ')
print(type(b))

a, b = map(int, input("Введите числа a и b через пробел: ").split())
print(a + b)