n = int(input("Ваше число "))
def f(n):
    if (1 <= n <= 2) or (n == 12):
        return "Зима"
    elif 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "Лето"
    elif 9 <= n <= 11:
        return "Осень"
print(f(n))