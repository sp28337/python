import functools
from typing import Callable
#
#
# # calls = {}
#
# class Counter:
#     calls = {}
#
#     def __call__(self, *args, **kwargs):
#         if self.func.__name__ not in self.calls:
#             self.calls[self.func.__name__] = 1
#         else:
#             self.calls[self.func.__name__] += 1
#         self.call_info()
#         return self.func(*args, **kwargs)
#
#     def __init__(self, func):
#         self.func = func
#
#     def call_info(self):
#         print('Function {0} was called {1} times'.format(self.func.__name__, self.calls[self.func.__name__]))
#
#
# # def counter(func: Callable) -> Callable:
# #     def wrapp_func(*args, **kwargs):
# #         global calls
# #         if func.__name__ not in calls:
# #             calls[func.__name__] = 1
# #         else:
# #             calls[func.__name__] += 1
# #         result = func(*args, **kwargs)
# #         print('Function {0} was called {1} times'.format(func.__name__, calls[func.__name__]))
# #         return result
# #     return wrapp_func
#
#
# @Counter
# def test_func(val):
#     return val ** 2
#
#
# @Counter
# def test_func2(val):
#     return val ** 3
#
#
# @Counter
# def test_func3(val):
#     return val ** 4
#
#
# # print(test_func.calls)
# test = test_func(4)
# test3 = test_func(434)
# # print(test_func.calls)
# test2 = test_func2(5)
# # print(test_func2.calls)
# print(Counter.calls)
