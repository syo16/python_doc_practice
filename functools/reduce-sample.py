import functools
from itertools import accumulate

print(functools.reduce(lambda x,y: x+y, range(10)))
print(list(accumulate(range(10))))

#実装
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


print(reduce(lambda x,y: x+y, range(10)))
