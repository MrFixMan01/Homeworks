def func():
    n = input("Введите число: ")
    b = list()
    while n != "":
        n = int(n)
        b.append(n)
        n = input("Введите число: / Завершите ввод: ")
    return b
