# Task 1. How are you?
#
# def how_are_you(func):
#     print('How are you? Good.\nBut I’m not very good! Okay, keep your function.')
#     res = func
#     return res
#
#
# @how_are_you
# def test():
#     print('<Something is going on here...>')
#
#
# test()


# Task 2. Slowing code
# import time
# import functools
# from typing import Callable, Any
#
#
# def wait_5_sec(func: Callable) -> Callable:
#     time.sleep(2)
#     result = func
#     return result
#
#
# @wait_5_sec
# def check_web_page() -> str:
#     return 'Web page checking...'
#
#
# print(check_web_page())
# print(check_web_page())


# Task 3. Logging
# from typing import Callable, Any, List
# import functools
# import datetime
#
#
# def logging(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs):
#         print('Documentation of function {0}:\n{1}'.format(func.__name__, func.__doc__))
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             print(e)
#             date = datetime.datetime.now()
#             with open('function_errors.log', 'a') as file:
#                 file.write('{2}|Error <{0}> in function <{1}>\n'.format(e, func.__name__, date))
#     return wrapped_func
#
#
# @logging
# def some_func(val: int) -> Any:
#     """Some func"""
#
#     lst = val ** 3
#     return lst
#
#
# print(some_func(val=67))
