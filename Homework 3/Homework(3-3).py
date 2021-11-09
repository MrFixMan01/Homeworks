n = int(input("Введите кол-во  "))
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = ' ')      #end = '' пишет все а в одну строку, без этого было в столбик
        a, b = b, a + b
fib(n)