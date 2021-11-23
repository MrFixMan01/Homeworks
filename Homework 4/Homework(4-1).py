from hm31 import func


def sdvig(b, n):
    for i in range(n):
        b = b[-1:] + b[:-1]
    return b


b = func()
n = int(input("На сколько сместить? "))
print(sdvig(b, n))
assert sdvig([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
assert sdvig([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert sdvig([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
assert sdvig([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]
assert sdvig([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
