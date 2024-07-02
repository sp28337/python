# Task 1. How are you?
#
# def how_are_you(func):
#     print('How are you? Good.\nBut I’m not very good! Okay, keep your function.')
#     res = func
#     return res
#
#
# @how_are_you
# def test():
#     print('<Something is going on here...>')
#
#
# test()


# Task 2. Slowing code
# import time
# import functools
# from typing import Callable, Any
#
#
# def wait_5_sec(func: Callable) -> Callable:
#     time.sleep(2)
#     result = func
#     return result
#
#
# @wait_5_sec
# def check_web_page() -> str:
#     return 'Web page checking...'
#
#
# print(check_web_page())
# print(check_web_page())
