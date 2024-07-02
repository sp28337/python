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
