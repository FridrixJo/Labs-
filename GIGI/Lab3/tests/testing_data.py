import math

i = 2


class Block:
    width = 19

    @staticmethod
    def get_width():
        return Block.width

    def get_volume(self):
        return self.width * 3


class Calc:
    @staticmethod
    def get_cos(v):
        return math.cos(v + i)


class C(Block, Calc):
    pass


def test_func(a):
    return math.sin(a - i)


def decorated_func(func):
    def wrapper(*args, **kwargs):
        print("start func")
        res = func(*args, **kwargs)
        print("end func")
        return res

    return wrapper
