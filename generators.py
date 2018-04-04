import itertools
import functools


# 1. Create alternative range func
# custom range generator
def custom_range(start, end, step=1):
    while start < end:
        yield start
        start = start + step

nums = custom_range(0, 5)
print("Custom range -- START --")
try:
    for i in nums:
        print(i)
        # influence on generator --> increase each value by one
        nums.send(i + 1)
except StopIteration:
    pass
print("Custom range -- END --")


# 2. Itertools

print("Itertools chain -- START --")
a = filter(lambda x: x % 2 == 0, range(4))
b = filter(lambda x: x % 3 == 0, range(4))
for i in itertools.chain(a, b):
    print(i)
print("Itertools chain -- END --")


print("Itertools product -- START --")
a = filter(lambda x: x % 2 == 0, range(4))
b = filter(lambda x: x % 3 == 0, range(4))
for i in itertools.product(a, b):
    print(i)
print("Itertools product -- END --")


print("Itertools compress -- START --")
a = filter(lambda x: x, range(4))
for i in itertools.compress(a, [1, 0, 1, 0]):
    print(i)
print("Itertools compress -- END --")

print("Itertools islice -- START --")
a = filter(lambda x: x, range(10))
for i in itertools.islice(a, 5, 8):
    print(i)
print("Itertools islice -- END --")


# 3. Recursion (factorial)
print("Recursion --START--")


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

print(factorial(5) == functools.reduce(lambda x, y: x * y, range(1, 6)))

print("Recursion -- END --")
