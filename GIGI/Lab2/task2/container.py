import random
import re



class Container:

    def __init__(self, user: str = 'pavel'):
        self.users = {user,}
        self.current_user = user
        self.storage: dict[str, set] = {user: set()}

    def add(self, *keys):
        for key in keys:
            self.storage[self.current_user].add(key)
            self.storage[self.current_user].discard('')

    def remove(self, key):
        if key in self.storage[self.current_user]:
            self.storage[self.current_user].discard(key)
        else:
            raise KeyError('there is no suck key')

    def list(self):
        for key, value in self.storage.items():
            print(key, ':', value)

    def find(self, *keys):
        for key in keys:
            if self.storage[self.current_user].intersection({key,}):
                print(f'key: {key} exists')
            else:
                print(f'key: {key} does not exist')

    def grep(self, regex):
        for i in self.storage[self.current_user]:
            if re.search(regex, i):
                print(i)

    def save(self):
        with open(f'{self.current_user}.txt', 'w') as file:
            file.write(f'{self.current_user} {" ".join(str(i) for i in self.storage[self.current_user])}\n')


    def load(self):
        with open(f'{self.current_user}.txt', 'r') as file:
            temp_dict = {}
            for line in file:
                data_arr = line.replace('\n', "").split(' ')
                self.storage[self.current_user] = set(data_arr[1:])
                temp_dict[self.current_user] = set(data_arr[1:])

            return temp_dict

    def switch(self, new_user: str = None):
        if new_user:
            self.current_user = new_user
            self.storage[new_user] = set()
            self.users.add(new_user)
        else:
            if len(self.users):
                self.current_user = random.choice(list(self.users))











