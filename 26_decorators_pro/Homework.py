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


# Task 3. Logging in format
# from datetime import datetime
# from functools import wraps
# from collections.abc import Callable
# from typing import Optional, Any
# import time
#
#
# def date_format_verify(format_str: str) -> str:
#     """Verify <format_str> for correct format"""
#
#     if not isinstance(format_str, str):
#         raise TypeError('Argument must be a string')
#     if len([x for x in format_str if x.isalpha()]) != 6:
#         raise TypeError('Wrong format. Exemple: <d.m.Y - H:M:S>')
#     format_str = ''.join(['%' + x if x.isalpha() else x for x in format_str])
#     return format_str
#
#
# def log_methods(_func: Optional[Callable] = None, mode="b d Y - H:M:S") -> Callable:
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         def wrapper(*args, **kwargs) -> Any:
#             m = date_format_verify(mode)
#             now = datetime.now()
#             formatted_date = now.strftime(m)
#             st = time.time()
#             print(f' - launching "{func.__name__}", date and time: {formatted_date}')
#             res = func(*args, **kwargs)
#             print(f' - finishing "{func.__name__}", runtime = {round(time.time() - st, 3)} sec')
#             return res
#
#         return wrapper
#
#     if _func is None:
#         return decorator
#     return decorator(_func)
#
#
# def for_all_methods(decorator: Callable) -> Callable:
#     """
#     Decorator of class.
#
#     Get other decorator and applies it with all class methods
#     """
#     @wraps(decorator)
#     def decorate(cls):
#         for method in dir(cls):
#             if method.startswith('__') is False:
#                 current_method = getattr(cls, method)
#                 decorated_method = decorator(current_method)
#                 setattr(cls, method, decorated_method)
#         return cls
#
#     return decorate
#
#
# @for_all_methods(log_methods)
# class A:
#     def __str__(self):
#         return 'A'
#
#     def test_sum_1(self) -> int:
#         print('test sum 1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
#
# @for_all_methods(log_methods)
# class B(A):
#
#     def __str__(self):
#         return 'B'
#
#     def test_sum_1(self):
#         super().test_sum_1()
#         print("Наследник test sum 1")
#
#     def test_sum_2(self):
#         print("test sum 2")
#         number = 200
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
#
# my_obj = B()
# my_obj.test_sum_1()
# my_obj.test_sum_2()


# Task 4. All world is - decorator
# from collections.abc import Callable
# from functools import wraps
#
#
# def decorator_with_args_for_any_decorator(decorator):
#     def wrapper(*args, **kwargs):
#         def wrapped_decorator(func: Callable) -> Callable:
#             return decorator(func, *args, **kwargs)
#         return wrapped_decorator
#     return wrapper
#
#
# @decorator_with_args_for_any_decorator
# def decorated_decorator(func: Callable, *args, **kwargs):
#     def inner(*inner_args, **inner_kwargs):
#         print(f"Переданные арг и кварги в декоратор: {args} {kwargs}")
#         return func(*inner_args, **inner_kwargs)
#
#     return inner
#
#
# @decorated_decorator(100, 'рублей', 200, 'друзей')
# def decorated_function(text: str, num: int) -> None:
#     print("Привет", text, num)
#
#
# decorated_function("Юзер", 101)
