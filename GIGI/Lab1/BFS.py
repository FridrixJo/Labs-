# from collections import deque
#
# dict = {}
#
# dict["you"] = ["bob", "alex", "alice"]
# dict["alice"] = []
# dict["bob"] = ["john", "damm"]
# dict["john"] = []
# dict["damm"] = []
# dict["alex"] = ["alinda", "meksim", "henry"]
# dict["alinda"] = []
# dict["meksim"] = []
# dict["henry"] = []
#
# print(dict)
#
#
# def BFSmango(dict):
#     search_queue = deque()
#     search_queue += dict["you"]
#     print(len(search_queue))
#     while search_queue:
#         person = search_queue.popleft()
#
#         if person[-1] == 'm':
#             print(f'{person} is mango seller')
#             return
#         else:
#             search_queue += dict[person]
#
#
# BFSmango(dict)
#
#
# class Hola:
#     def __init__(self, phrase):
#         self.phrase = phrase
#
#     def __call__(self, *args, **kwargs):
#         print(self.phrase)
#
#
# hey = Hola('SUck my balls')
#
# hey()



import requests
import time


def wrapper(func):
    def inner():
        sec = time.time()
        func()
        print(f'Time: {time.time() - sec} seconds')
    return inner


# @wrapper
def get_data():
    url = "https://api.binance.com/api/v3/ticker/price"
    # params = {'symbol': 'BTCUSDT'}

    response = requests.get(url)
    data = response.json()
    return data


# print(get_data())

# price = data['price']
# print(f"The latest price of BTC/USDT is {price}")

import asyncio
import httpx


# @wrapper
async def get_latest_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    # params = {"symbol": "BTCUSDT"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        # price = data["price"]
        return data


async def main():
    price = await get_latest_price()
    print(f"The latest price of BTC/USDT is {price}")


# asyncio.run(main())


class Person:
    def __hash__(self):
        return 1


a = Person()
b = Person()
c = Person()
d = {}
d[a] = "hola1"
d[b] = "hola2"
d[(1,2, 3, 4)] = [1, 2, 3]
print(d.items())
for key, value in d.items():
    print(key, value)
print(d)

seq = range(100)
print(type(seq))
print(list(seq))

seq = [{'age': 10, 'love': True}, {'age': 30}, {'age': 20}]

seq.sort(key=lambda user: user.get('age'))
print(seq)


def wrapper(func: callable):
    def inner(*args, **kwargs):
        print('hola')
        func(*args, **kwargs)
        print(len(args), len(kwargs))
        print('bye')
    return inner

@wrapper
def my_func(a, b, c, d):
    print(a, b, c, d)

my_func(a=1, b=2, c=3, d=4)

