x = (input("Введите число "))
b = list()
while x != '':
    b.append(x)
    x = (input("Еще одно "))
else:
    b.sort(reverse=True)
    if int(b[0]) > int(b[1]):
        b[1], b[0] = b[0], b[1]
        print(("Итого "), *b, sep ='')
    else:
        print(("Итого "), *b, sep ='')
