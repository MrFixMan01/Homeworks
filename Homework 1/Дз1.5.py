x=float(input("Введите х"))
y=float(input("Введите у"))
if x > 0 and y > 0:
    print("1-я четверть")
elif y > 0 and x < 0:
    print("2-я четверть")
elif y < 0 and x < 0:
    print("3-я четверть")
elif x > 0 and y < 0:
    print("4-я четверть")
else:
    print("Точка лежит на оси")
