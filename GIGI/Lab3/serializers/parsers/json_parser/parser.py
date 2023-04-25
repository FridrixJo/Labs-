from serializers.parsers.parser_interface import Parser


class JSONParser(Parser):
    def dump(self, obj, fp):
        pass

    def dumps(self, obj) -> str:
        pass

    def load(self, fp):
        pass

    def loads(self, s):
        pass
