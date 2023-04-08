print('hola')
from container import Container

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

    main_menu()

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
            regex = str(input("enter a regular exp"))
            print(container.grep(regex))
        elif n == 6:
            container.save()
        elif n == 7:
            temp_dict = container.load()
            print(temp_dict)
        elif n == 8:
            user = str(input('enter new user'))
            container.switch(user)
        else:
            print('wrong input')


if __name__ == "__main__":
    main()

