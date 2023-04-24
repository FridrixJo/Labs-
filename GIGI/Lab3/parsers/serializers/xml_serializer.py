from parsers.serializers.abstract_serializer import AbstractSerializer
from parsers.serializers.parser_interface import Parser
from parsers.xml_parser.parser import XMLParser


class XMLSerializer(AbstractSerializer):
    def create_serializer(self) -> Parser:
        return XMLParser()
