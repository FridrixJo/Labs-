import random

print('hola')
from container import Container
#
# a = Container()
# a.load()
# a.list()
# a.add(1, 45, 5, 1, 45)
# a.list()
# a.switch('ilya')
# a.list()
# a.save()
# a.load()

# a = Container()
# a.load()
# print(a.current_user)
# a.switch()
# print(a.current_user)
# a.add(54, 'fdihjfi')
# a.list()
# a.find(54, 22)
# a.remove('andrew')
# a.list()
# a.save()
a = random.choice(list(set()))
print(a)

# a = set()
# a.add('hola')
# a.add('slaa')
# for i in a:
#     print(i)


def main_menu():
    print('0 - exit')
    print('1 - add')
    print('2 - remove')
    print('3 - find')
    print('4 - list')
    print('5 - grep')
    print('6 - save')
    print('7 - load')
    print('8 - switch')

def main():
    username = input('Enter username: ')
    while not username:
        username = input('Enter username: ')

    container = Container(username)

    while True:
        n = 0
        try:
            n = int(input('enter n: '))
        except Exception:
            pass

        if n == 0:
            break
        elif n == 1:
            data = (input("enter data to add: ")).split(" ")
            container.add(*data)
        elif n == 2:
            key = str(input("enter key to delete"))
            container.remove(key)
        elif n == 3:
            data = (input("enter data to add: ")).split(" ")
            container.find(*data)
        elif n == 4:
            container.list()
        elif n == 5:




