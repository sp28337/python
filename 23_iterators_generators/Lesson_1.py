# Task 1. My for
#
# def my_for(iterable):
#     try:
#         iterator = iterable.__iter__()
#         while True:
#             print(iterator.__next__())
#     except StopIteration:
#         return None
#     except AttributeError as e:
#         print('Error! Argument must be an iterable.')
#
#
# lst = [1, 2, 4, 5]
# my_for(lst)
