import re
import inspect
import types
from constans import CODE_ATTRS, BASE_TYPE, BASE_COLLECTIONS


def serialize(obj) -> dict:
    data = dict()
    obj_type = type(obj)

    if isinstance(obj, (list, tuple, set, frozenset, bytearray, bytes)):
        data["type"] = get_base_type(obj_type)
        data["value"] = [serialize(ser_obj) for ser_obj in obj]
    elif isinstance(obj, dict):
        data["type"] = get_base_type(obj_type)
        data["value"] = [serialize([k, v]) for (k, v) in obj.items()]
    elif isinstance(obj, (str, int, float, bool, complex)):
        data["type"] = get_base_type(obj_type)
        data["value"] = obj
    elif inspect.isfunction(obj):
        data["type"] = "function"
        data["value"] = serialize_function(obj)
    elif inspect.iscode(obj):
        data["type"] = "code"
        args = dict()
        for k, v in inspect.getmembers(obj):
            if k in CODE_ATTRS:
                args[k] = serialize(v)
        data["value"] = args
    elif isinstance(obj, types.CellType):
        data["type"] = "cell"
        data["value"] = serialize(obj.cell_contents)
    elif inspect.isclass(obj):
        data["type"] = "class"
        data["value"] = serialize_object(obj)
    elif not obj:
        data["type"] = "NoneType"
        data["value"] = "Null"
    else:
        data["type"] = "object"
        data["value"] = serialize_object(obj)

    return data


def get_base_type(obj_type):
    return re.search(r"\'(\w+)\'", str(obj_type))[1]


def serialize_function(func, cls=None):
    if not inspect.isfunction(func):
        return

    ser_value_func = dict()
    ser_value_func["__name__"] = func.__name__
    ser_value_func["__globals__"] = get_globals(func, cls)

    if func.__closure__:
        ser_value_func["__closure__"] = serialize(func.__closure__)
    else:
        ser_value_func["__closure__"] = serialize(tuple())

    args = dict()

    for k, v in inspect.getmembers(func.__code__):
        if k in CODE_ATTRS:
            args[k] = serialize(v)

    ser_value_func["__code__"] = args

    return ser_value_func


def get_globals(func, cls=None):
    glob = dict()

    for glob_var in func.__code__.co_names:
        if glob_var in func.__globals__:
            if isinstance(func.__globals__[glob_var], types.ModuleType):
                glob["module " + glob_var] = serialize(
                    func.__globals__[glob_var].__name__
                )

            elif inspect.isclass(func.__globals__[glob_var]):
                if (cls and func.__globals__[glob_var] != cls) or (not cls):
                    glob[glob_var] = serialize(func.__globals__[glob_var])

            elif glob_var != func.__code__.co_name:
                glob[glob_var] = serialize(func.__globals__[glob_var])

            else:
                glob[glob_var] = serialize(func.__name__)

    return glob


def serialize_class(obj):
    ser = dict()
    ser["__name__"] = serialize(obj.__name__)

    for mem in obj.__dict__:
        member = [mem, obj.__dict__[mem]]
        if member[0] in (
            "__name__",
            "__base__",
            "__basicsize__",
            "__dictoffset__",
            "__class__",
        ) or type(member[1]) in (
            types.WrapperDescriptorType,
            types.MethodDescriptorType,
            types.BuiltinFunctionType,
            types.GetSetDescriptorType,
            types.MappingProxyType,
        ):
            continue

        if member[0] == "ret_bob" and False:
            print("\n\nBOB")
            print(mem, obj.__dict__)
            print(member[1], serialize_function(member[1].__func__, obj))
        if isinstance(obj.__dict__[member[0]], staticmethod):
            ser[member[0]] = {
                "type": "staticmethod",
                "value": {
                    "type": "function",
                    "value": serialize_function(member[1].__func__, obj),
                },
            }
        elif isinstance(obj.__dict__[member[0]], classmethod):
            ser[member[0]] = {
                "type": "classmethod",
                "value": {
                    "type": "function",
                    "value": serialize_function(member[1].__func__, obj),
                },
            }
        elif inspect.ismethod(member[1]):
            ser[member[0]] = serialize_function(member[1].__func__, obj)

        elif inspect.isfunction(member[1]):
            ser[member[0]] = {"type": "function", "value": serialize_function(member[1], obj)}
        else:
            ser[member[0]] = serialize(member[1])
    ser["__bases__"] = {
        "type": "tuple",
        "value": [serialize(base) for base in obj.__bases__ if base != object],
    }
    return ser


def serialize_object(obj):
    ser = dict()
    ser["__class__"] = serialize(obj.__class__)
    members = dict()

    for k, v in inspect.getmembers(obj):
        if k.startswith("__") or inspect.isfunction(v) or inspect.ismethod(v):
            continue
        members[k] = serialize(v)

    ser["__members__"] = members

    return ser


def deserialize(obj: dict):
    # print(obj, type(obj))
    if obj["type"] in BASE_TYPE:
        return generator_type(obj["type"], obj["value"])

    elif obj["type"] in BASE_COLLECTIONS:
        return gener_collection(obj["type"], obj["value"])

    elif obj["type"] == "dict":
        return dict(gener_collection("list", obj["value"]))

    elif obj["type"] == "function":
        return deserialize_function(obj["value"])

    elif obj["type"] == "code":
        code = obj["value"]
        return types.CodeType(
            deserialize(code["co_argcount"]),
            deserialize(code["co_posonlyargcount"]),
            deserialize(code["co_kwonlyargcount"]),
            deserialize(code["co_nlocals"]),
            deserialize(code["co_stacksize"]),
            deserialize(code["co_flags"]),
            deserialize(code["co_code"]),
            deserialize(code["co_consts"]),
            deserialize(code["co_names"]),
            deserialize(code["co_varnames"]),
            deserialize(code["co_filename"]),
            deserialize(code["co_name"]),
            deserialize(code["co_firstlineno"]),
            deserialize(code["co_lnotab"]),
            deserialize(code["co_freevars"]),
            deserialize(code["co_cellvars"]),
        )

    elif obj["type"] == "cell":
        return types.CellType(deserialize(obj["value"]))

    elif obj["type"] == "class":
        return deserialize_class(obj["value"])

    elif obj["type"] == "staticmethod":
        return staticmethod(deserialize(obj["value"]))

    elif obj["type"] == "classmethod":
        return classmethod(deserialize(obj["value"]))

    elif obj["type"] == "object":
        return deserialize_object(obj["value"])


def generator_type(_type, obj):
    if _type == "int":
        return int(obj)
    elif _type == "float":
        return float(obj)
    elif _type == "complex":
        return complex(obj)
    elif _type == "str":
        return str(obj)
    elif _type == "bool":
        return bool(obj)


def gener_collection(_type, obj):
    if _type == "list":
        return list(deserialize(o) for o in obj)
    elif _type == "tuple":
        return tuple(deserialize(o) for o in obj)
    elif _type == "set":
        return set(deserialize(o) for o in obj)
    elif _type == "frozenset":
        return frozenset(deserialize(o) for o in obj)
    elif _type == "bytearray":
        return bytearray(deserialize(o) for o in obj)
    elif _type == "bytes":
        return bytes(deserialize(o) for o in obj)


def deserialize_function(obj):
    # print(obj)
    code = obj["__code__"]
    globs = obj["__globals__"]
    closures = obj["__closure__"]
    res_globs = dict()

    for k in obj["__globals__"]:
        if "module" in k:
            res_globs[globs[k]["value"]] = __import__(globs[k]["value"])

        elif globs[k] != obj["__name__"]:
            res_globs[k] = deserialize(globs[k])

    closure = tuple(deserialize(closures))

    codeType = types.CodeType(
        deserialize(code["co_argcount"]),
        deserialize(code["co_posonlyargcount"]),
        deserialize(code["co_kwonlyargcount"]),
        deserialize(code["co_nlocals"]),
        deserialize(code["co_stacksize"]),
        deserialize(code["co_flags"]),
        deserialize(code["co_code"]),
        deserialize(code["co_consts"]),
        deserialize(code["co_names"]),
        deserialize(code["co_varnames"]),
        deserialize(code["co_filename"]),
        deserialize(code["co_name"]),
        deserialize(code["co_firstlineno"]),
        deserialize(code["co_lnotab"]),
        deserialize(code["co_freevars"]),
        deserialize(code["co_cellvars"]),
    )

    funcRes = types.FunctionType(code=codeType, globals=res_globs, closure=closure)
    funcRes.__globals__.update({funcRes.__name__: funcRes})

    return funcRes


def deserialize_class(obj):
    bases = deserialize(obj["__bases__"])
    members = dict()

    for member, value in obj.items():
        members[member] = deserialize(value)

    clas = type(deserialize(obj["__name__"]), bases, members)

    for k, member in members.items():
        if inspect.isfunction(member):
            member.__globals__.update({clas.__name__: clas})
        elif isinstance(member, (staticmethod, classmethod)):
            member.__func__.__globals__.update({clas.__name__: clas})
    return clas


def deserialize_object(obj):
    clas = deserialize(obj["__class__"])
    members = dict()

    for k, v in obj["__members__"].items():
        members[k] = deserialize(v)

    res = object.__new__(clas)
    res.__dict__ = members

    return res
