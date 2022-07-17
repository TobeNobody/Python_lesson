# import time
# seconds = int(input("Введите время в секундах: "))
# print(time.strftime('%H:%M:%S', time.gmtime(seconds)))

seconds = int(input('Введите время в секундах: '))
minutes = seconds % 3600 // 60
hours = seconds // 3600
sek = seconds % 3600 % 60
print(f"{hours:02}:{minutes:02}:{sek:02}")