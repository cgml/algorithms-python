def move_zeros(a):
    zeroidx, nonzeroidx = 0, 0
    while zeroidx < len(a) and nonzeroidx < len(a):
        while zeroidx < len(a) and a[zeroidx] != 0: zeroidx += 1
        nonzeroidx = max(zeroidx, nonzeroidx)
        while nonzeroidx < len(a) and a[nonzeroidx] == 0: nonzeroidx+=1
        if zeroidx < nonzeroidx and nonzeroidx < len(a):
            a[zeroidx], a[nonzeroidx], zeroidx, nonzeroidx = a[nonzeroidx], 0, zeroidx+1, nonzeroidx+1
    return a

assert move_zeros([0,1,0,3,12]) == [1,3,12,0,0]
assert move_zeros([1,3,12]) == [1,3,12]
assert move_zeros([1,3,12,0,0]) == [1,3,12,0,0]
assert move_zeros([0,0,0,1,0,3,12,0,0]) == [1,3,12,0,0,0,0,0,0]
assert move_zeros([0,0,0,1,3,12]) == [1,3,12,0,0,0]
assert move_zeros([0,1,0,3,12]) ==  [1,3,12,0,0]