INT = r"[+-]?\d+"
FLOAT = r"([+-]?\d+(\.\d+))"
STR = r"\"((\\\")|[^\"])*\""
BOOL = r"\b(true|false)\b"
NONE = r"\b(Null)\b"

LIST_RECURSION = r"\[(?R)?(,(?R))*\]"
VALUE_RECURSION = r"\{((?R):(?R))?(,(?R):(?R))*\}"

VALUE = rf"\s*({LIST_RECURSION}|{VALUE_RECURSION}|{STR}|{FLOAT}|{BOOL}|{INT}|{NONE}\s*)"
