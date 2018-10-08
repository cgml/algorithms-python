def f(N):
    for i in range(N):
        yield i
        yield i+i
        yield i*i


print([x for x in f(10)])

print([i for sl in (lambda x:[(y, y + y, y * y) for y in range(x)])(10) for i in sl])

print([(r,c,v) for r in range(3) for c in range(3) for v in range(3)])

nums = [[0,1],[2,3]]
print([nums[r][c] for r in range(len(nums)) for c in range(len(nums[0]))])
print(list(zip(*nums)))

