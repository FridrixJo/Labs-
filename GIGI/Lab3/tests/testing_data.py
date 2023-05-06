import math

i = 2


class A:
    a = 1

    @staticmethod
    def get_arg():
        return A.a

    def test_method(self):
        return self.a / 2


class B:

    @staticmethod
    def get_cos(v):
        return math.cos(v + i)


class C(A, B):
    pass


def test_func(a):
    return math.sin(a - i)

def dec(func):
    def wrapper(*args, **kwargs):
        print('start func')
        res = func(*args, **kwargs)
        print('end func')
        return res
    return wrapper
