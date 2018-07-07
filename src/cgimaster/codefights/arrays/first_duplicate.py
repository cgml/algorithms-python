def first_duplicate(a):
    for x in a:
        if a[abs(x) - 1] < 0: return abs(x)
        a[abs(x) - 1] *= -1
    return -1


assert first_duplicate([2, 3, 3, 1, 5, 2]) == 3