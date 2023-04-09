import math

summa = int(input("Введите сумму чисел: "))
multiply = int(input("Введите произведение чисел: "))

d = summa ** 2 - 4 * multiply

if d >= 0:
    x1 = int((summa + math.sqrt(d)) / 2)
    x2 = int((summa - math.sqrt(d)) / 2)
    y1 = summa - x1
    y2 = summa - x2
    print(f"Результат №1 : [{x1}, {y1}]")
    print(f"Результат №2 : [{x2}, {y2}]")
else:
    print("Дискриминант не может быть меньше 0!")