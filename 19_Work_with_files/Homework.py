# Task 1. Summa of nubers 2
#
# import os
#
#
# numbers_file = open(os.path.abspath('numbers.txt'))
# summ = 0
#
# print('Content of file numbers.txt:')
# data_1 = numbers_file.read()
# print(data_1)
#
# numbers_file.seek(0)
#
# for i_elem in numbers_file:
#     lst = i_elem.split()
#     if '\n'.join(lst).isdigit():
#         summ += int(i_elem)
#
#
# answer_file = open('answer.txt', 'w')
# answer_file.write(str(summ))
#
# answer_file.close()
# numbers_file.close()
#
# print('Content of file answer.txt:')
# answer_file = open('answer.txt')
# data_2 = answer_file.read()
# print(data_2)


# Task 2. Python's dzen

# import os
#
# zen_file = open('zen.txt')
# data = zen_file.read()
# lst = list()
#
# for i_line in data.split('\n'):
#     lst.append(i_line)
# zen_file.close()
# lst.reverse()
# print('\n'.join(lst))


# Task 3. Dzen of Python 2
#
# letters, words, strings = 0, 0, 0
# min_letter = 'a'
#
# zen_file = open('zen.txt')
# # Find out strings count
# for i_line in zen_file:
#     strings += 1
#
# zen_file.seek(0)
# # Find out letters count
# data = zen_file.read()
# for letter in data.lower():
#     if letter.isalpha():
#         letters += 1
#         # Find out min letter
#         if data.count(letter) < data.count(min_letter):
#             min_letter = letter
#
# # Find out words count
# words = len(data.split())
#
# zen_file.close()
#
# print(f'Letters {letters}\nWords {words}\nStrings {strings}\nMin letter {min_letter}')


# Task 4. Files and folders
#
# import os
#
#
# def path_info(path, dirs=[], files=[], size=[]):
#     for i_elem in os.listdir(path):
#         if os.path.isdir(os.path.join(path, i_elem)):
#             dirs.append(1)
#             path_info(os.path.join(path, i_elem))
#         if os.path.isfile(os.path.join(path, i_elem)):
#             files.append(1)
#             size.append(os.path.getsize(os.path.join(path, i_elem)))
#     return dirs, files, size
#
#
# abs_path = os.path.abspath('')
# print(abs_path)
#
# count_dirs, count_files, size_klb = path_info(abs_path)
# print(f'Catalog size(klb): {sum(size_klb) / 1024}\n'
#       f'Count of sub-catalogs: {sum(count_dirs)}\n'
#       f'Count of files: {sum(count_files)}')
