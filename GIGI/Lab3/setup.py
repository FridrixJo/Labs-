from setuptools import setup

setup(
    name="fj_serializer",
    packages=[
        "serializers",
        "serializers/parsers",
        "serializers/parsers/json_parser",
        "serializers/parsers/xml_parser",
        "serializers/constants"
    ],
    version="0.2.0",
    description="python custom objects serializer. created by Fridrix Jo",
    author="FridrixJo",
    author_email="pglutov@gmail.com",
    license="MIT",
    install_requires=["regex==2023.5.4"],
    python_requires=">=3.10",
)
