res = []

k = {1:[1,2], 2:[3,4]}

res.extend(v for v in k[1])
res.extend(v for v in k[2])
print(res)