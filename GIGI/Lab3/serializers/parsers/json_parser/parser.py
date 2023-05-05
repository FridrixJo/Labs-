import regex

from serializers.constants.json_serializer_constants import (
    INT,
    FLOAT,
    BOOL,
    NONE,
    STR,
    VALUE,
)


class JSONParser:
    def dumps(self, obj):
        return self.inner_dumps(obj)

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def loads(self, string):
        return self.inner_loads(string)

    def load(self, file):
        return self.loads(file.read())

    def inner_dumps(self, value):
        if isinstance(value, str):
            return (
                '"'
                + value.replace("\\", "\\\\").replace('"', '"').replace("'", "'")
                + '"'
            )

        elif isinstance(value, (int, float, complex, bool)):
            return str(value).lower()

        elif isinstance(value, dict):
            return (
                "{"
                + ", ".join(
                    [
                        f"{self.inner_dumps(key)}:{self.inner_dumps(value)}"
                        for key, value in value.items()
                    ]
                )
                + "}"
            )

        elif isinstance(value, list):
            return "[" + ", ".join([self.inner_dumps(val) for val in value]) + "]"

    def inner_loads(self, string):
        string = string.strip()

        result = regex.fullmatch(INT, string)
        if result:
            return int(result.group(0))

        result = regex.fullmatch(FLOAT, string)
        if result:
            return float(result.group(0))

        result = regex.fullmatch(BOOL, string)
        if result:
            return result.group(0) == "true"

        result = regex.fullmatch(NONE, string)
        if result:
            return None

        result = regex.fullmatch(STR, string)
        if result:
            res = result.group(0)
            res = res.replace("\\\\", "\\").replace(r"\"", '"').replace(r"\'", "'")
            return res[1:-1]

        if string[0] == "[" and string[-1] == "]":
            string = string[1:-1]
            result = regex.findall(VALUE, string)
            return [self.inner_loads(match[0]) for match in result]

        if string[0] == "{" and string[-1] == "}":
            string = string[1:-1]
            result = regex.findall(VALUE, string)
            return {
                self.inner_loads(result[i][0]): self.inner_loads(result[i + 1][0])
                for i in range(0, len(result), 2)
            }
