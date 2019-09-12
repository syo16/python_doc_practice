from functools import partial

def add(a, b, c):
    return a + b + c

add_two = partial(add, 2)

print(add_two(2, 3))

basetwo = partial(int, base=2)
print(basetwo('1010101010'))
print(int('1010101010', base=2))
