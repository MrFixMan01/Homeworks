from hm31 import func


def f2(b):
    lst1 = list(set(b))
    if b == lst1:
        return True
    else:
        return False
b = func()
print(f2(b))
assert f2([1, 2, 3, 3]) == False
assert f2([1, 2, 3, 4, 5]) == True
