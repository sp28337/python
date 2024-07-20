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

