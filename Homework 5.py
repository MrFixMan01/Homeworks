d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def binary_search(d, n):
    lower = 0
    upper = len(d) - 1
    while lower <= upper:
        center = (lower + upper) // 2
        if d[center] == n:
            return center
        elif d[center] > n:
            upper = center - 1
        elif d[center] < n:
            lower = center + 1
    return None


n = int(input("Элемент, который необходимо обнаружить: "))
print(binary_search(d, n))
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == 1
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == None
assert binary_search([], 10) == None
assert binary_search([1, 2, 2, 3, 4, 5, 6, 7, 8, 9], 2) == 1
