from setuptools import setup

setup(
    name='custom_serializer',
    packages=['serializers', 'serializers/parsers'],
    version='0.1.0',
    description='python custom objects serializer',
    author='FridrixJo',
    license='MIT',
    install_requires=['regex==2023.5.4'],
    python_requires=">=3.10",
)
