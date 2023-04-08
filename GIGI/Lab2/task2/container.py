import random
import re

class Container:

    def __init__(self, user: str = 'pavel'):
        self.users = {user,}
        self.current_user = user
        self.storage: dict[str, set] = {user: set()}

    def add(self, *keys):
        if self.current_user:
            try:
                for key in keys:
                    self.storage[self.current_user].add(key)
            except Exception:
                print('wrong keys')
        else:
            print('add user')

    def remove(self, key):
        try:
            if self.storage[key]:
                del self.storage[key]
                self.users.discard(key)
                if key == self.current_user:
                    if len(self.users):
                        self.current_user = random.choice(list(self.users))
                    else:
                        self.current_user = None
        except Exception:
            print('wrong key')

    def list(self):
        for key, value in self.storage.items():
            print(key, ':', value)

    def find(self, *keys):
        if self.current_user:
            try:
                for key in keys:
                    if self.storage[self.current_user].intersection({key,}):
                        print(f'key: {key} exists')
                    else:
                        print(f'key: {key} does not exist')
            except Exception:
                print('wrong keys')
        else:
            print('add user')

    def grep(self, regex):
        if self.current_user:
            status = False
            for i in self.storage[self.current_user]:
                if re.search(regex, i):
                    print(i)
            if status is False:
                print('Not found')
        else:
            print('add user')

    def save(self):
        with open('container.txt', 'w') as file:
            for i in self.users:
                file.write(f'{i} {" ".join(str(i) for i in self.storage[i])}\n')


    def load(self):
        with open('container.txt', 'r') as file:
            for line in file:
                data_arr = line.replace('\n', "").split(' ')
                self.users.add(data_arr[0])
                self.current_user = data_arr[0]
                self.storage[data_arr[0]] = set(data_arr[1:])


    def switch(self, new_user: str = None):
        if new_user:
            self.current_user = new_user
            self.storage[new_user] = set()
            self.users.add(new_user)
        else:
            if len(self.users):
                self.current_user = random.choice(list(self.users))
            else:
                self.current_user = None











