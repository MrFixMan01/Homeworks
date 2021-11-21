def sim(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k += 1
    if k <= 0:
        return True
    else:
        return False
a = int(input("Введите число "))
print(sim(a))