import types

CODE_ATTRIBUTES = (
    "co_argcount",
    "co_posonlyargcount",
    "co_kwonlyargcount",
    "co_nlocals",
    "co_stacksize",
    "co_flags",
    "co_code",
    "co_consts",
    "co_names",
    "co_varnames",
    "co_filename",
    "co_name",
    "co_firstlineno",
    "co_lnotab",
    "co_freevars",
    "co_cellvars",
)

OBJECT_ATTRIBUTES = (
    "__name__",
    "__base__",
    "__basicsize__",
    "__dictoffset__",
    "__class__",
)

USELESS_FIELDS = (
    types.WrapperDescriptorType,
    types.MethodDescriptorType,
    types.BuiltinFunctionType,
    types.GetSetDescriptorType,
    types.MappingProxyType,
)

BASE_TYPES = ("int", "float", "complex", "str", "bool")
BASE_COLLECTIONS = ("list", "tuple", "set", "frozenset", "bytearray", "bytes")
