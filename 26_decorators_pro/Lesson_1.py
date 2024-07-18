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


# Task 2. Directories
# import os
# from contextlib import contextmanager
# import pprint
#
#
# @contextmanager
# def in_dir(path: str) -> str:
#     if not os.path.exists(path):
#         raise NameError('There are not such path like this')
#     yield path
#
#
# try:
#     with in_dir(os.path.abspath(os.path.join(os.sep, 'home', 'sp28337', "projects", 'pythdon'))) as p:
#         pprint.pprint(os.listdir(p))
# except Exception as e:
#     print(e)

