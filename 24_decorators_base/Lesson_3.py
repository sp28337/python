# Task 1. Sandwich
# from typing import Callable, Any
#
#
# def bread(func: Callable) -> Callable:
#     def wrapped_func(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return '</----------\\>\n{}\n<\\__________/>'.format(result)
#
#     return wrapped_func
#
#
# def filling(func: Callable) -> Callable:
#     def wrapped_func(*args: Any, **kwargs: Any) -> str:
#         result = func(*args, **kwargs)
#         return '  #{0}#\n{1}\n   ~{2}~'.format('tomatoes', result, 'salad')
#     return wrapped_func
#
#
# @bread
# @filling
# def sandwich(instance: str) -> str:
#     return ' ----{}----  '.format(instance)
#
#
# test1 = sandwich('meet')
# print(test1)


# Task 2. Plugins
# from typing import Callable, Any
#
# PLUGINS = dict()
#
#
# def register(func: Callable) -> Callable:
#     PLUGINS[func.__name__] = func
#     return func
#
#
# @register
# def say_hallo(name: str) -> str:
#     return 'Hello {}!'.format(name)
#
#
# @register
# def say_goodbye(name: str) -> str:
#     return 'Goodbye {}!'.format(name)
#
#
# test = say_hallo('Thai')
# print(test)
# print(PLUGINS)
