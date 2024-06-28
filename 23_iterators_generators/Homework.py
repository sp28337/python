# Task 1. Squares
# from collections.abc import Iterable
#
#
# class Iterator:
#
#     def __init__(self, num: int) -> None:
#         self.__num = num
#         self.__counter = 0
#
#     def __iter__(self) -> None:
#         return self
#
#     def __next__(self) -> Iterable[int]:
#         while self.__counter < self.__num:
#             self.__counter += 1
#             return self.__counter ** 2
#         else:
#             raise StopIteration
#
#
# def iter_gen(num):
#     counter = 0
#     while counter < num:
#         counter += 1
#         yield counter ** 2
#
#
# user_number = int(input('Enter the number: '))
# test1 = Iterator(user_number)
# for i in test1:
#     print(i, end=' ')
#
# print()
#
# test2 = iter_gen(user_number)
# for j in test2:
#     print(j, end=' ')
#
# print()
#
# test3 = (x ** 2 for x in range(1, user_number + 1))
# for k in test3:
#     print(k, end=' ')
