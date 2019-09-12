import functools
import time

@functools.lru_cache(maxsize=None)
def fib1(n):
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

start = time.time()

for i in range(35):
    print(fib1(i))

print('Total time(lru_cache):', time.time() - start)

start = time.time()

for i in range(35):
    print(fib2(i))

print('Total time(without lru_cache):', time.time() - start)
