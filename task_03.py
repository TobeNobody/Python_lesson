
def my_func(a, b, c):
    if a < b and a < c:
        print(b + c)
    elif b < a and b < c:
        print(a + c)
    elif c < a and c < b:
        print(a + b)
    else:
        print("Есть равные значения!")

my_func(int(input('Введите значения а: ')), int(input('Введите значения b: ')),
        int(input('Введите значения c: ')))



