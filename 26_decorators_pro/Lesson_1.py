# Task 1. Timer context manager (decorator)
# from contextlib import contextmanager
# from collections.abc import Iterable
# import time
#
#
# @contextmanager
# def timer() -> Iterable:
#     st = time.time()
#     try:
#         yield
#     except Exception as e:
#         print(e)
#     finally:
#         print(f"Total time: {time.time() - st}")
#
#
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# with timer() as t:
#     print(get_nod("94", 846))
