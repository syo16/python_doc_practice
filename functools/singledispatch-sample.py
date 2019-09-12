from functools import singledispatch

@singledispatch
def func(arg, verbose=False):
    if verbose:
        print('Let me just say', end='')
    print(arg)

@func.register
def _(arg:int, verbose=False):
    if verbose:
        print('Value---->', end='')
    print(arg)

@func.register
def _(arg:list, verbose=False):
    if verbose:
        print('Show all elements')
    for element in arg:
        print(element, end=' ')
    print()

func([2, 3, 4, 5])
func(33, verbose=True)
