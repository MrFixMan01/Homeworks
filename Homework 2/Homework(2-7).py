import random

z = int(input("Введите ваше число"))
x = random.randint(0, 100)
while x != z:
    if z < x:
        print("Загаданное число больше!")
    elif x < z:
        print("Загаданное число меньше!")
    z = int(input())
print("Вы угадали число!")