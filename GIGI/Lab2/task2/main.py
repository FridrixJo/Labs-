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
        try:
            n = int(input('enter n: '))
        except Exception:
            print('wrong value, N has to be number')
            continue

        if n == 0:
            print('thanks for using')
            break
        elif n == 1:
            data = (input("enter data to add through whitespace: ")).split(" ")
            container.add(*data)
        elif n == 2:
            key = str(input("enter key to delete: "))
            try:
                container.remove(key)
            except KeyError:
                print('there is no such key in your collection')
        elif n == 3:
            data = (input("enter data to add through whitespace: ")).split(" ")
            container.find(*data)
        elif n == 4:
            container.list()
        elif n == 5:
            regex = str(input("enter a regular exp: "))
            container.grep(regex)
        elif n == 6:
            container.save()
            print('data was saved')
        elif n == 7:
            temp_dict = container.load()
            print(temp_dict)
        elif n == 8:
            user = str(input('enter new user: '))
            container.switch(user)
            print(f'current user: {container.current_user}')
        else:
            print('wrong input')


if __name__ == "__main__":
    main()

