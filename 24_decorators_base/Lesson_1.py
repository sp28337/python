# Task 1. Functions
# from typing import Callable, Any
#
#
# def func_1(x: int) -> int:
#     return x + 10
#
#
# def func_2(func: Callable, *args, **kwargs):
#     result = func(*args, **kwargs)
#     return result ** 2
#
#
# print(func_2(func_1, 9))


# Task 2. Timer
# import time
# from typing import Callable, Any
#
#
# def timer(func: Callable, *args, **kwargs):
#     start = time.time()
#     result = func(*args, **kwargs)
#     end = time.time()
#     total_t = round(end - start, 4)
#     print('Total time:', total_t)
#     return result
#
#
# def find_factorial(num):
#     if num == 1:
#         return 1
#     fact_n_minus_1 = find_factorial(num - 1)
#     return fact_n_minus_1 * num
#
#
# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
#
#
# test1 = timer(power, 100.24, 19)
# print(test1)
