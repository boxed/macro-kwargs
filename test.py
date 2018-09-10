# noinspection PyUnresolvedReferences
from macros import macros, grab


def foo(a, b, c):
    return a + b + c


def test():
    a = 1
    b = 2
    c = 3

    print(foo(**grab[a, b, c]))


test()
