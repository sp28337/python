# import datetime
#
# def create_datetime(cls):
#     def wrapper(*args, **kwargs):
#         instance = cls(*args, **kwargs)
#         print(f'{cls} instance creation time: {datetime.datetime.now(datetime.UTC)}')
#         return instance
#     return wrapper
#
#
# @create_datetime
# class Functions:
#     def __init__(self, max_num: int) -> None:
#         self.max_num = max_num
#
#     def cubes_sum(self, number: int) -> int:
#         result = 0
#         for _ in range(number):
#             result += sum([x ** 3 for x in range(self.max_num)])
#         return result
#
#     def squares_sum(self, number: int) -> int:
#         result = 0
#         for _ in range(number):
#             result += sum([x ** 2 for x in range(self.max_num)])
#         return result
#
#
# test1 = Functions(max_num=1000)
# test2 = Functions(max_num=2000)
# test3 = Functions(max_num=3000)
#
# print(test1.__class__)
# print(test2)
# print(test3)


# Task 1. Access rights
from functools import wraps
# from typing import Optional, Union, Any
# from collections.abc import Callable
#
# user_permissions = ['admin']
#
#
# def check_permission(_func: Optional[Callable] = None, rights: str = 'unknown') -> Callable:
#     def decorator(func: Callable) -> Callable:
#         def wrapper(*args, **kwargs) -> Any:
#             try:
#                 if rights in user_permissions:
#                     res = func(*args, **kwargs)
#                     return res
#                 raise PermissionError(f'PermissionError: User haven\'t access rights to use function <{func.__name__}>')
#             except PermissionError as e:
#                 print(e)
#
#         return wrapper
#
#     if _func is None:
#         return decorator
#     return decorator(_func)
#
#
# @check_permission(rights='admin')
# def delete_site() -> None:
#     print('Удаляем сайт')
#
#
# @check_permission
# def add_comment() -> None:
#     print('Добавляем комментарий')
#
#
# delete_site()
# add_comment()


# Task 2. Callback function
# import os
# import pprint
#
#
# def callback(_func=None, path='/'):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             pprint.pprint(f"list dirs: {os.listdir(path)}")
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#
#     if _func is None:
#         return decorator
#     return decorator(_func)
#
#
# class App:
#
#     def get(self, path):
#         if os.path.exists(path):
#             return self.example
#         return None
#
#     @callback
#     def example(self):
#         print('Пример функции, которая возвращает ответ сервера')
#         return 'OK'
#
#
# app = App()
# route = app.get('/')
# if route:
#     response = route()
#     print('Ответ:', response)
# else:
#     print('Такого пути нет')
