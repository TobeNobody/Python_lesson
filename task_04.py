number = int(input('Введите целое положительное число: '))
n = 0

while number > 10:
    last_digit = number % 10
    number //= 10
    if last_digit > n:
        n = last_digit

print(n)

