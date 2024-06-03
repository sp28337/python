# Task 1. Results
#
# import os
#
# def find_files(cur_path, name):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if name == i_elem:
#             return path
#         if os.path.isdir(path):
#             res = find_files(path, name)
#             if res:
#                 break
#     else:
#         res = None
#     return res
#
#
# def do_what_need(f):
#     what_do = input("What to do?('+', '-', '*')")
#     if what_do == '+':
#         summ = 0
#         for elem in f:
#             summ += int(elem.split()[2])
#         else:
#             print('Summa of points = {}'.format(summ))
#     elif what_do == '-':
#         diff = 0
#         for elem in f:
#             diff -= int(elem.split()[2])
#         else:
#             print('Difference of points = {}'.format(diff))
#     elif what_do == '*':
#         mult = 1
#         for elem in f:
#             mult *= int(elem.split()[2])
#         else:
#             print('Mult of points = {}'.format(mult))
#     else:
#         print("You must enter ('+', '-', '*')")
#         do_what_need(f)
#
#
# files_list = ['group_1.txt', 'group_2.txt']
#
# print('My files:')
# for index, file in enumerate(files_list):
#     print('{pos}) {name}'.format(pos=index + 1, name=file))
#
#
# index_file = int(input('For which file do you wanna find path? '))
#
# find_path = find_files(os.path.abspath(os.path.join('..', '..', '..', 'task')), files_list[index_file - 1])
# if find_path:
#     print('\nPath to file:', find_path, end='\n')
#     open_file = open(find_path, 'r', encoding='utf-8')
#     do_what_need(open_file)
# else:
#     print('None')
