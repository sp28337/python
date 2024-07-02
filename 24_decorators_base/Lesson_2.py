# Task 1. Double challenge
# from typing import Callable, Any
#
#
# def do_twice(func: Callable):
#     def wrapped_func(*args, **kwargs):
#         # script before function execution
#         result1 = func(*args, **kwargs)
#         result2 = func(*args, **kwargs)
#         # script after function execution
#         return result1, result2
#     return wrapped_func
#
#
# @do_twice
# def greeting(name):
#     print('Hello, {name}!'.format(name=name))
#
#
# greeting('Pattaya')
