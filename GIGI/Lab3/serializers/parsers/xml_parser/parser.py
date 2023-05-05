import regex

from serializers.constants.xml_serializer_constants import ELEMENT
from serializers.parsers.parser_interface import Parser


class XMLParser(Parser):
    def dumps(self, obj):
        return self.inner_dumps(obj)

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def loads(self, string):
        return self.inner_loads(string)

    def load(self, file):
        return self.loads(file.read())

    def inner_dumps(self, value):
        if isinstance(value, (int, float, bool)):
            return f"<{type(value).__name__}>{str(value)}</{type(value).__name__}>"

        elif isinstance(value, str):
            value = (
                value.replace('"', "&quot;")
                .replace("'", "&apos;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("&", "&amp;")
            )
            return f"<str>{value}</str>"

        elif isinstance(value, list):
            value = "".join([self.inner_dumps(val) for val in value])
            return f"<list>{value}</list>"

        elif isinstance(value, dict):
            value = "".join(
                [
                    f"{self.inner_dumps(key)}{self.inner_dumps(val)}"
                    for key, val in value.items()
                ]
            )
            return f"<dict>{value}</dict>"

        elif not value:
            return "<NoneType>None</NoneType>"

    def inner_loads(self, string):
        result = regex.fullmatch(ELEMENT, string)

        if not result:
            return

        key = result.group("key")
        value = result.group("value")

        match key:
            case "int":
                return int(value)

            case "float":
                return float(value)

            case "bool":
                return str(value) == "True"

            case "NoneType":
                return None

            case "str":
                return (
                    value.replace("&quot;", '"')
                    .replace("&apos;", "'")
                    .replace("&lt;", "<")
                    .replace("&gt;", ">")
                    .replace("&", "&amp;")
                )

            case "list":
                result = regex.findall(ELEMENT, value)
                return [self.inner_loads(match[0]) for match in result]

            case "dict":
                result = regex.findall(ELEMENT, value)
                return {
                    self.inner_loads(result[i][0]): self.inner_loads(result[i + 1][0])
                    for i in range(0, len(result), 2)
                }
