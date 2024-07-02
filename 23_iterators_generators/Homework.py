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


# Task 2. Refactoring
# from collections.abc import Iterable
#
#
# def find_gen(num_to_find: int, l1: list, l2: list) -> str:
#     for x in l1:
#         for y in l2:
#             yield '{0} * {1} = {2}'.format(x, y, x * y)
#             if x * y == num_to_find:
#                 print('Found!')
#                 return
#
#
# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
#
# test = find_gen(to_find, list_1, list_2)
# for i in test:
#     print(i)


# Task 3. File's paths
# import os
# from typing import Optional, Any
#
# def gen_files_path(target_dir: str = '23_iterators_generators',
#                    start_dir: str = os.path.abspath(os.path.join('/'))) -> Optional[list]:
#     try:
#         print('Start dir:', start_dir)
#         for element in os.listdir(start_dir):
#             if not element.startswith('.'):
#                 current_path = os.path.join(start_dir, element)
#                 print('    now at --- {}'.format(current_path))
#                 if os.path.isdir(current_path):
#                     if element == target_dir:
#                         list_files_path = [os.path.join(current_path, file)
#                                            if os.path.isfile(os.path.join(current_path, file))
#                                            else print('\nSEEKING WAS FINISHED\n')
#                                            for file in os.listdir(current_path)
#                                            ]
#
#                         return list_files_path
#
#                     result = gen_files_path(target_dir, current_path)
#                     if result:
#                         break
#         else:
#             result = None
#         return result
#     except PermissionError as e:
#         print(e)
#
#
# test1 = gen_files_path()
# print(test1)


# Task 4. Hofstadter sequence
#
# def q_hofstadter(s):
#     if s == [1, 1]:
#         a = s[:]
#         while True:
#             try:
#                 q = a[-a[-1]] + a[-a[-2]]
#                 a.append(q)
#                 yield q
#             except IndexError:
#                 return
#     else:
#         print('Передано неверное значение списка!\nПравильный список [1, 1]')
#
#
# Q = [1, 1]
#
# for i, number in enumerate(q_hofstadter(Q)):
#     if i <= 30:
#         print(number, end=', ')
#     else:
#         break

# Task 5. Count of strings
#
# import os
# from collections.abc import Iterable
#
#
# def total_strings(target_dir: str) -> Iterable:
#     for elem in os.listdir(target_dir):
#         if elem.endswith('.py'):
#             yield os.path.join(target_dir, elem)
#
#
# def count_in_file(path: Iterable) -> Iterable:
#     counter = 0
#     for i in path:
#         print(i)
#         with open(i, 'r', encoding='utf-8') as file:
#             for line in file:
#                 if not line.startswith('#') and not line == '\n':
#                     counter += 1
#     yield counter
#
#
# directory = os.path.abspath(os.path.join('..', input('Enter name of directory: ')))
# if os.path.exists(directory):
#     test2 = sum(count_in_file(total_strings(directory)))
#     print('\nCount of strings in directory: {}'.format(test2))
# else:
#     print('Error! Path not found')
