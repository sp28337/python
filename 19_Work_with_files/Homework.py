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


# Task 5. Preservation
# import os
#
#
# def save_file(txt):
#     user_path = input('\nWhere save the document? Input folder sequence(sep by space): ').split()
#     relation_path = os.path.join(*user_path)
#     if os.path.exists(os.path.abspath(os.path.join(os.path.sep, relation_path))):
#         file_name = input('\nInput file name: ') + '.txt'
#         abs_path = os.path.abspath(os.path.join(os.path.sep, relation_path, file_name))
#         if os.path.exists(abs_path):
#             user_approves = input(f'\nDo you really wanna resave file {file_name}? ')
#             if user_approves in ('y', 'ye', 'yes', 'ya', 'es', 'yess', 'yyy'):
#                 file_name_file = open(file_name, 'w', encoding='utf-8')
#                 file_name_file.write(txt)
#                 file_name_file.close()
#                 result = '\nFile successfully resaved.'
#                 return result, abs_path
#         else:
#             file_name_file = open(file_name, 'w', encoding='utf-8')
#             file_name_file.write(txt)
#             file_name_file.close()
#             result = '\nFile successfully saved.'
#             return result, abs_path
#     else:
#         result = '\nThere are not any path like that.'
#         return result, None
#
#
# text = input('Enter text: ')
# new_file, path = save_file(text)
# print(new_file)
#
# print('\nContent of file:')
# if path:
#     path_file = open(path)
#     data = path_file.read()
#     print(data)
#     path_file.close()
# else:
#     print('Error')


# Task 6. Paranoia
#
# import os
# import string
#
#
# def caesar_cipher(alph, encode, shift=1):
#     char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in encode.lower()]
#     return ''.join(char_list).title()
#
#
# alphabet = string.ascii_letters
# file_name = "text.txt"
#
# print('Content of file {name}:'.format(name=file_name))
# file_name_file = open(os.path.abspath(file_name), 'r', encoding='utf-8')
# list_strings = [x for x in file_name_file]
# for i in list_strings:
#     print(i, end='')
# file_name_file.close()
#
# cipher_text_file = open('cipher_text.txt', 'w')
# for index, val in enumerate(list_strings):
#     cipher_text_file.write(caesar_cipher(alphabet, val[:-1], shift=index + 1) + '\n')
# cipher_text_file.close()
#
# print('\nContent of file cipher_text.txt:')
# cipher_text_file = open('cipher_text.txt')
# data = cipher_text_file.read()
# cipher_text_file.close()
# print(data)


# Task 7. Tournament
#
# import os
#
#
# def get_data_from_file(path, lst_1t=None):
#     if lst_1t is None:
#         lst_1t = list()
#         lst_2t = list()
#         file = open(path, 'r', encoding='utf-8')
#         print('Content of file first_tour.txt:')
#         for row in file:
#             print(row, end='')
#             lst_1t.append(row[:-1].split())
#         file.close()
#
#         min_score_to_pass = int(lst_1t[0][0])
#
#         for line in lst_1t[1:]:
#             if int(line[2]) > min_score_to_pass:
#                 # Change surname and name places
#                 lst_2t.append([line[1][0] + '.', line[0], line[2]])
#
#         lst_2t = sorted(lst_2t, key=lambda player: player[2], reverse=True)
#         lst_2t.insert(0, str(len(lst_2t)))
#         return lst_1t, lst_2t
#     else:
#         print('ERROR')
#
#
# def make_file(name, lst):
#     file = open('second_tour.txt', 'w', encoding='utf-8')
#     for index, value in enumerate(lst):
#         if index == 0:
#             file.write(value + '\n')
#         else:
#             file.write(f'{index}) {" ".join(value)}\n')
#     file.close()
#
#
# def read_file(name):
#     print(f'\nContent of file {name}:')
#     second_tour_file = open(name)
#     data = second_tour_file.read()
#     print(data)
#     second_tour_file.close()
#
#
# first_tour_players_lst, to_second_tour_lst = get_data_from_file(os.path.abspath('first_tour.txt'))
# make_file('second_tour.txt', to_second_tour_lst)
# read_file('second_tour.txt')
