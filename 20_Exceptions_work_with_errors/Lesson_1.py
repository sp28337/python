# Task 1. Five element
#
# BRUCE_WILLIS = 42
#
# try:
#     input_data = input('Введите строку: ')
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError:
#     print('Impossible convert to a number!')
# except IndexError:
#     print('Index out of range')


# Task 2. Age
#
# import string
# import os
#
#
# def make_file(name1, name2):
#     if os.path.exists(os.path.abspath(name2)):
#         print('This file already exists!')
#     else:
#         dct = {}
#         try:
#             with open(name1, 'r', encoding='utf-8') as my_file:
#                 for index, row in enumerate(my_file):
#                     dct.setdefault(alphabet[index], row[:-1])
#
#             with open(name2, 'w', encoding='utf-8') as new_f:
#                 for key, value in dct.items():
#                     new_f.write(' '.join((key, value, '\n')))
#         except FileNotFoundError:
#             print('File not found')
#         except PermissionError:
#             print('Error! This is a directory')
#         except (TypeError, ValueError):
#             print('Wrong data type or wrong value!')
#
#
# alphabet = string.ascii_lowercase
# file_name = 'ages.txt'
# new_file = 'result1.txt'
# make_file(file_name, new_file)
