import re
import inspect
import types

from serializers.constants.object_constants import (
    CODE_ATTRIBUTES,
    OBJECT_ATTRIBUTES,
    USELESS_FIELDS,
)


def get_base_type(object_type):
    return re.search(r"\'([.\w]+)\'", str(object_type))[1]


def serialize_function_type(func, class_obj=None):
    if not inspect.isfunction(func):
        return

    result = dict()

    args = dict()
    result["__name__"] = func.__name__
    result["__globals__"] = get_global_vars(func, class_obj)

    if func.__closure__:
        result["__closure__"] = serialize(func.__closure__)
    else:
        result["__closure__"] = serialize(tuple())

    for key, value in inspect.getmembers(func.__code__):
        if key in CODE_ATTRIBUTES:
            args[key] = serialize(value)

    result["__code__"] = args

    return result


def get_global_vars(func, class_obj=None):
    result = dict()
    func_globals = func.__globals__

    for global_var in func.__code__.co_names:
        if global_var in func_globals:
            if isinstance(func_globals[global_var], types.ModuleType):
                result["module " + global_var] = serialize(
                    func_globals[global_var].__name__
                )

            elif inspect.isclass(func_globals[global_var]):
                if (
                    class_obj and func.__globals__[global_var] != class_obj
                ) or not class_obj:
                    result[global_var] = serialize(func_globals[global_var])

            elif global_var != func.__code__.co_name:
                result[global_var] = serialize(func_globals[global_var])

            else:
                result[global_var] = serialize(func.__name__)

    return result


def serialize_class_type(class_obj):
    result = dict()
    # print('CLASS', class_obj.__name__, 'TYPE', type(class_obj.__name__))
    result["__name__"] = serialize(class_obj.__name__)

    for attribute_name in class_obj.__dict__:
        attribute_value = class_obj.__dict__[attribute_name]

        if (
            attribute_name in OBJECT_ATTRIBUTES
            or type(attribute_value) in USELESS_FIELDS
        ):
            continue

        if isinstance(class_obj.__dict__[attribute_name], (staticmethod, classmethod)):
            if isinstance(class_obj.__dict__[attribute_name], staticmethod):
                ser_type = "staticmethod"
            else:
                ser_type = "classmethod"

            result[attribute_name] = {
                "type": ser_type,
                "value": {
                    "type": "function",
                    "value": serialize_function_type(
                        attribute_value.__func__, class_obj
                    ),
                },
            }

        elif inspect.ismethod(attribute_value):
            result[attribute_name] = serialize_function_type(
                attribute_value.__func__, class_obj
            )

        elif inspect.isfunction(attribute_value):
            result[attribute_name] = {
                "type": "function",
                "value": serialize_function_type(attribute_value, class_obj),
            }

        else:
            result[attribute_name] = serialize(attribute_value)

    result["__bases__"] = {
        "type": "tuple",
        "value": [serialize(base) for base in class_obj.__bases__ if base != object],
    }

    return result


def serialize_object_type(obj):
    result = dict()
    result["__class__"] = serialize(obj.__class__)

    members = dict()

    for key, value in inspect.getmembers(obj):
        if (
            not key.startswith("__")
            and not inspect.isfunction(value)
            and not inspect.ismethod(value)
        ):
            members[key] = serialize(value)

    result["__members__"] = members

    return result


def serialize(obj):
    result = dict()
    base_object_type = get_base_type(type(obj))

    if isinstance(obj, (str, int, float, bool, complex)):
        result["type"] = base_object_type
        result["value"] = obj

    elif isinstance(obj, (list, tuple, set, frozenset, bytearray, bytes)):
        result["type"] = base_object_type
        result["value"] = [serialize(enclosed_obj) for enclosed_obj in obj]

    elif isinstance(obj, dict):
        result["type"] = base_object_type
        result["value"] = [serialize([key, value]) for (key, value) in obj.items()]

    elif isinstance(obj, types.CellType):
        result["type"] = "cell"
        result["value"] = serialize(obj.cell_contents)

    elif inspect.isfunction(obj):
        result["type"] = "function"
        result["value"] = serialize_function_type(obj)

    elif inspect.isclass(obj):
        result["type"] = "class"
        result["value"] = serialize_class_type(obj)

    elif inspect.iscode(obj):
        result["type"] = "code"
        args = dict()

        for key, value in inspect.getmembers(obj):
            if key in CODE_ATTRIBUTES:
                args[key] = serialize(value)

        result["value"] = args

    elif not obj:
        result["type"] = "NoneType"
        result["value"] = "Null"

    else:
        result["type"] = "object"
        result["value"] = serialize_object_type(obj)

    return result
