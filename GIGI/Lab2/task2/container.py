import random
import re

class Container:

    def __init__(self):
        self.users = ['pavel']
        self.current_user = 'pavel'
        self.storage: dict[str, set] = {'pavel': set()}

    def add(self, *keys):
        try:
            for key in keys:
                self.storage[self.current_user].add(key)
        except Exception:
            print('wrong keys')

    def remove(self, key):
        try:
            self.storage[self.current_user].discard(key)
        except Exception:
            print('wrong key')

    def list(self):
        for key, value in self.storage.items():
            print(key, ':', value)

    def find(self, keys):
        try:
            print(self.storage[self.current_user].intersection(set(keys)))
        except Exception:
            print('wrong keys')

    def grep(self, regex):
        status = False
        for i in self.storage[self.current_user]:
            if re.search(regex, i):
                print(i)
        if status is False:
            print('Not found')

    def save(self):
        with open('container.txt') as file:
            for i in self.users:
                file.write(f'{i}: {self.storage[i]} \n')


    def switch(self, new_user: str=None):
        if new_user:
            self.current_user = new_user
            self.storage[new_user] = set()
            self.users.append(new_user)
        else:
            if len(self.users):
                self.current_user = random.choice(self.users)


    # def load(self):








