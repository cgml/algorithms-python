# A simple generator for Fibonacci Numbers
def fib(limit):
    yield "START: "
    a, b = 0, 1
    while a < limit:
        if a: yield a
        a, b = b, a + b
    yield ":EOM"

# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())

# Loops & Comprehensions
for i in fib(5): print(i, end=",")

print([x for x in fib(5)])