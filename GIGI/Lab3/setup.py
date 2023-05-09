from setuptools import setup

setup(
    name="jo_serializer",
    packages=[
        "serializers",
        "serializers/parsers",
        "serializers/parsers/json_parser",
        "serializers/parsers/xml_parser",
    ],
    version="0.1.1",
    description="python custom objects serializer",
    author="FridrixJo",
    author_email="pglutov@gmail.com",
    license="MIT",
    install_requires=["regex==2023.5.4"],
    python_requires=">=3.10",
)
