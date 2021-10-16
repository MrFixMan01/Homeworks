s = input("Введите строку ")
num = int(input("Номер элемента, который необходимо вывести "))
a = []
for i in s:
    if i in "0123456789":
        a.append(i)
print(a[num - 1])