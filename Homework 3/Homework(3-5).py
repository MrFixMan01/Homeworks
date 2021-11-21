def sred(b):
    s = sum(b) / len(b)
    print("Среднее арифметическое =", s)
n = input("Ввод ")
b = list()
while n != '':
    b.append(float(n))
    n = input("Ввод ")
sred(b)