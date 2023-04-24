from parsers.serializers.json_serializer import JSONSerializer
from parsers.serializers.xml_serializer import XMLSerializer


def create_serializer(serializer: str):
    if serializer.upper() == 'JSON':
        return JSONSerializer().create_serializer()
    if serializer.upper() == 'XML':
        return XMLSerializer().create_serializer()
