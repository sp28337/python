# Task 1. Repeating code
# from functools import wraps
#
#
# def repeat(times=2):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#
#             for time in range(times):
#                 func(*args, **kwargs)
#             return None
#         return wrapper
#     return decorator
#
#
# @repeat(times=10)
# def some_func(n):
#     """Test func"""
#     t = 1
#     for i in range(1, n + 1):
#         t *= i ** 3
#     print(t, some_func.__doc__)
#
#
# some_func(10)


# Task 2. Slowing down code
# import math
# import time
# from collections.abc import Callable
# from typing import Optional
#
#
# def dx_decorator(_func: Optional[Callable] = None, *, dx: float = 0.01, sleep: int = 1) -> Callable:
#     def func_decorator(func: Callable) -> Callable:
#         def wrapper(x: int, *args, **kwargs) -> float:
#             print('processing...')
#             time.sleep(sleep)
#             res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#         return wrapper
#     if _func is None:
#         return func_decorator
#     return func_decorator(_func)
#
#
# @dx_decorator(sleep=0.3)
# def sin_dx(x: int) -> float:
#     return math.sin(x)
#
#
# for d in range(1, 11):
#     r = sin_dx(d)
#     print(f'производная в точке {d} = {r}')
