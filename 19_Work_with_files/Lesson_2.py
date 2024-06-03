# Task 1. Icons
# import os.path
#
#
# def what_is_it(path):
#     if os.path.isfile(path):
#         print('This is a file\nSize of file:', os.path.getsize(path), 'bytes')
#     elif os.path.isdir(path):
#         print('This is a directory')
#     elif os.path.islink(path):
#         print('This is a link')
#     else:
#         print('This path does not exist')
#
#
# input_path = input('Enter a path: ')
# what_is_it(input_path)


# Task 2. Seeking files
# import os
#
#
# def find_files(abspath, file_name):
#     for i_elem in os.listdir(abspath):
#         path = os.path.join(abspath, i_elem)
#         if i_elem == file_name:
#             print('   ', path)
#         if os.path.isdir(path):
#             find_files(path, file_name)
#
#
# input_abspath = os.path.abspath(os.path.join('..'))
# file_to_find = input('Enter file name what you wanna find: ')
# find_files(input_abspath, file_to_find)
