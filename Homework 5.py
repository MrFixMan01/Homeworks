d = [2, 2, 2, 2, 2, 2]
def binary_search(d, n):
    lower = 0
    upper = len(d) - 1
    while lower <= upper:
        center = (lower + upper) // 2
        if d[center] == n:
            for i in range(center + 1):
                if d[i] == d[center] and i < center:
                    center = i
            return center
        elif d[center] > n:
            upper = center - 1
        elif d[center] < n:
            lower = center + 1
    return None


n = int(input("Элемент, который необходимо обнаружить: "))
print(binary_search(d, n))
assert binary_search([], 42) == None
assert binary_search([0], 0) == 0
assert binary_search([0], 1) == None
assert binary_search([-1, 0, 42], 0) == 1
assert binary_search([-42, 0, 42], 42) == 2
assert binary_search([-6, -5, -4, -3, -2, -1], -4) == 2
assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert binary_search([1, 2, 3, 4, 5], 7) == None
assert binary_search([1, 2, 3, 4, 5, 6], 7) == None
assert binary_search([42, 42, 42, 42, 42], 42) == 0
assert binary_search([-42, -42, -42, -42, -42], -42) == 0
assert binary_search([42, 42, 42, 42, 43], 43) == 4
assert binary_search([41, 42, 42, 42, 42], 41) == 0
assert binary_search([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert binary_search([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4
assert binary_search([2, 2, 2, 2, 2, 2], 2) == 0