from hm31 import func


def f1(b):
    print("\tЭлемент", "|", "\tЧастота")
    for x in set(b):
        y = b.count(x)
        print("\t", x, "\t|", "\t", y)
b = func()
f1(b)
