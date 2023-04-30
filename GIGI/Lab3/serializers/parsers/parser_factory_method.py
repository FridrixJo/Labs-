from serializers.parsers.json_parser.parser import JSONParser
from serializers.parsers.xml_parser.parser import XMLParser


def create_parser(name):
    name.lower()
    if name == "json":
        return JSONParser()
    if name == "xml":
        return XMLParser()
    raise Exception("There is no such parser")
