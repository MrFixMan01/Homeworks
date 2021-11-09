def sred(b):
    s = sum(b) / len(b)
    print("Среднее арифметическое =", s)
b = list()
n = (input("Ввод  "))
while n != "":
    b.append(float(n))
    n = (input("Ввод "))
sred(b)