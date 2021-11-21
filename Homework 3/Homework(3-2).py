def f(n):
    if n in (1, 2, 12):
        return "Зима"
    elif 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "Лето"
    elif 9 <= n <= 11:
        return "Осень"
n = int(input("Ваше число "))
print(f(n))