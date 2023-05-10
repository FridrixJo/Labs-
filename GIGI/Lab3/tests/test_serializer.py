import random
import unittest
from serializers.serializer import Serializer
from tests.testing_data import Block, C, test_func, decorated_func


class SerializerTests(unittest.TestCase):
    def setUp(self):
        self.serializer = Serializer(
            random.choice(
                (
                    "json",
                    "xml",
                )
            )
        )

    def test_int(self):
        ser = self.serializer.dumps(10)
        print(ser)
        des = self.serializer.loads(ser)
        print(des)

        self.assertEqual(des, 10)

    def test_float(self):
        ser = self.serializer.dumps(10.1)
        des = self.serializer.loads(ser)

        self.assertEqual(des, 10.1)

    def test_str(self):
        ser = self.serializer.dumps("hi!")
        des = self.serializer.loads(ser)

        self.assertEqual(des, "hi!")

    def test_list(self):
        lst = [1, 2, 3, 4, [5, 6], [7, "the"], "end."]

        ser = self.serializer.dumps(lst)
        des = self.serializer.loads(ser)

        self.assertEqual(des, lst)

    def test_tuple(self):
        tpl = (1, 2, 3, 4, (5, 6), (7, "the"), "end.")

        ser = self.serializer.dumps(tpl)
        des = self.serializer.loads(ser)

        self.assertEqual(des, tpl)

    def test_dict(self):
        dct = {"a": 1, "b": 2, "c": {"d": "e"}, 1: 90}

        ser = self.serializer.dumps(dct)
        des = self.serializer.loads(ser)

        self.assertEqual(des, dct)

    def test_set(self):
        st = {1, 3, 4, 5, 5, 3, "fkfk"}

        ser = self.serializer.dumps(st)
        des = self.serializer.loads(ser)

        self.assertEqual(des, st)

    def test_func(self):
        ser = self.serializer.dumps(test_func)
        des = self.serializer.loads(ser)

        self.assertEqual(des(10), test_func(10))

    def test_lambda_func(self):
        lambda_func = lambda x: x * 2

        ser = self.serializer.dumps(lambda_func)
        des = self.serializer.loads(ser)

        self.assertEqual(lambda_func(10), des(10))

    def test_classmethod(self):
        obj = C()
        ser = self.serializer.dumps(obj)
        des = self.serializer.loads(ser)

        self.assertEqual(obj.get_volume(), des.get_volume())

    def test_staticmethod(self):
        ser = self.serializer.dumps(Block)
        des = self.serializer.loads(ser)

        self.assertEqual(Block.get_width(), des.get_width())

    def test_decorator(self):
        dec_func = decorated_func(test_func)

        ser = self.serializer.dumps(decorated_func)
        des = self.serializer.loads(ser)

        des_func = des(test_func)

        self.assertEqual(dec_func(10), des_func(10))
