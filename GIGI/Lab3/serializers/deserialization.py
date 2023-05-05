import types
import inspect

from serializers.constants.object_constants import (
    BASE_TYPES,
    BASE_COLLECTIONS,
    CODE_ATTRIBUTES,
)


def deserialize_base_type(obj_type, obj):
    if obj_type == "int":
        return int(obj)
    elif obj_type == "float":
        return float(obj)
    elif obj_type == "complex":
        return complex(obj)
    elif obj_type == "str":
        return str(obj)
    elif obj_type == "bool":
        return bool(obj)


def deserialize_base_collection(obj_type, obj):
    if obj_type == "list":
        return list(deserialize(element) for element in obj)
    elif obj_type == "tuple":
        return tuple(deserialize(element) for element in obj)
    elif obj_type == "set":
        return set(deserialize(element) for element in obj)
    elif obj_type == "frozenset":
        return frozenset(deserialize(element) for element in obj)
    elif obj_type == "bytearray":
        return bytearray(deserialize(element) for element in obj)
    elif obj_type == "bytes":
        return bytes(deserialize(element) for element in obj)


def deserialize_class(class_obj):
    bases = deserialize(class_obj["__bases__"])
    items = dict()

    for item, value in class_obj.items():
        items[item] = deserialize(value)

    cls = type(deserialize(class_obj["__name__"]), bases, items)

    for item in items.values():
        if inspect.isfunction(item):
            item.__globals__.update({cls.__name__: cls})

        elif isinstance(item, (staticmethod, classmethod)):
            item.__func__.__globals__.update({cls.__name__: cls})

    return cls


def deserialize_object(obj):
    cls = deserialize(obj["__class__"])
    items = dict()

    for key, value in obj["__members__"].items():
        items[key] = deserialize(value)

    res = object.__new__(cls)
    res.__dict__ = items

    return res


def deserialize_function(func_obj):
    code = func_obj["__code__"]
    func_globals = func_obj["__globals__"]
    closures = func_obj["__closure__"]
    final_globals = dict()

    for key in func_globals:
        if "module" in key:
            final_globals[func_globals[key]["value"]] = __import__(
                func_globals[key]["value"]
            )

        elif func_globals[key] != func_obj["__name__"]:
            final_globals[key] = deserialize(func_globals[key])

    closures = tuple(deserialize(closures))
    code = types.CodeType(
        *tuple(deserialize(code[attribute]) for attribute in CODE_ATTRIBUTES)
    )

    res = types.FunctionType(code=code, globals=final_globals, closure=closures)
    res.__globals__.update({res.__name__: res})

    return res


def deserialize(obj):
    if obj["type"] in BASE_TYPES:
        return deserialize_base_type(obj["type"], obj["value"])

    elif obj["type"] in BASE_COLLECTIONS:
        return deserialize_base_collection(obj["type"], obj["value"])

    elif obj["type"] == "dict":
        return dict(deserialize_base_collection("list", obj["value"]))

    elif obj["type"] == "code":
        code = obj["value"]
        return types.CodeType(
            *tuple(deserialize(code[attribute]) for attribute in CODE_ATTRIBUTES)
        )

    elif obj["type"] == "function":
        return deserialize_function(obj["value"])

    elif obj["type"] == "class":
        return deserialize_class(obj["value"])

    elif obj["type"] == "staticmethod":
        return staticmethod(deserialize(obj["value"]))

    elif obj["type"] == "classmethod":
        return classmethod(deserialize(obj["value"]))

    elif obj["type"] == "object":
        return deserialize_object(obj["value"])

    elif obj["type"] == "cell":
        return types.CellType(deserialize(obj["value"]))
