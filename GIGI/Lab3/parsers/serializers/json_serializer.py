from parsers.json_parser.parser import JSONParser
from parsers.serializers.abstract_serializer import AbstractSerializer
from parsers.serializers.parser_interface import Parser


class JSONSerializer(AbstractSerializer):
    def create_serializer(self) -> Parser:
        return JSONParser()
