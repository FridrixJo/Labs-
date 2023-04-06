import re

class Container:

    def __init__(self):
        self.name = ''
        self.storage: dict[str, set] = {}

    def __add__(self, keys: list):
        try:
            for key in keys:
                self.storage[self.name].add(key)
        except Exception:
            print('wrong keys')

    def remove(self, key):
        try:
            self.storage[self.name].discard(key)
        except Exception:
            print('wrong key')

    def list(self):
        print(self.storage[self.name])

    def find(self, keys):
        try:
            print(self.storage[self.name].intersection(set(keys)))
        except Exception:
            print('wrong keys')

    def grep(self, regex):
        status = False
        for i in self.storage[self.name]:
            if re.search(regex, i):
                print(i)
        if status is False:
            print('Not found')

    def save(self):
        with open('container.txt') as file:
            for i in self.

    def load(self):








