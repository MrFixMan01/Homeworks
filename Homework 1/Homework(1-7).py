m = 0
x = int(input("Ведите х "))
y = int(input("Введите у "))
for i in range(x, y + 1):
    if i % 5 == 0:
        m += i
print(m)