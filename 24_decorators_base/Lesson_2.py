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


# Task 2. Timer 2
# import time
# from typing import Callable, Any
#
#
# def timer(func: Callable) -> Callable:
#     """Decorator for check running time of a function"""
#
#     def wrapped_func(*args: Any, **kwargs: Any) -> Any:
#         start = time.time()
#         result = func(*args, **kwargs)
#         finish = time.time()
#         total_t = round(finish - start, 4)
#         print('Function was running for {} seconds'.format(total_t))
#         return result
#
#     return wrapped_func
#
#
# @timer
# def rand_function(num: int) -> int:
#     total = 0
#     for i in range(num):
#         total += sum([j**3 for j in range(1, 100)])
#     return total
#
#
# result = rand_function(10000)
# print(result)
