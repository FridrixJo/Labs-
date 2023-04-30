from serializers.serializer import Serializer

a = Serializer("xml")


def func():
    return 1 + 1


print(a.dumps(func))

