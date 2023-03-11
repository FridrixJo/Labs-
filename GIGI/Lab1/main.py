print('hola')


def parametrized_wrapper(*args):
    def wrapper(func: callable):
        def inner():
            print('start')
            func()
            print('end')
            for i in args:
                print(i)
        return inner
    return wrapper


@parametrized_wrapper(1, 23, "ofijihfruijfr")
def my_func():
    print('say hola')


my_func()

def make_operation(n, m, operation):
    match operation:
        case "add":
            return n + m
        case "sub":
            return n - m
        case "mul":
            return n * m
        case "div":
            return n / m


operation = input("input data .. ")

print(make_operation(13, 4, operation))


