a = int(input("Введите a="))
b = int(input("Введите b="))
c = int(input("Введите c="))
d = int(input("Введите d="))
f = int(input("Введите f="))
e = f - d
if e == 0:
    print("Делить на ноль нельзя!")
else:
    x = (a * b - c) / e
    print(x)
