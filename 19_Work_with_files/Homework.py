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


# Task 8. Frequency analysis
import os
#
#
# def my_sort(lst):
#     """This function for sorting data"""
#
#     lst.sort(key=lambda x: x[1], reverse=True)
#
#     count_lst = list()
#     for i, val in enumerate(lst):
#         if i == len(lst):
#             break
#         else:
#             if val[1] != lst[(i + 1) % len(lst)][1]:
#                 count_lst.append(i)
#
#     for j, v in enumerate(count_lst):
#         if j == 0:
#             lst[:v + 1] = sorted(lst[:v + 1])
#         else:
#             lst[j + 1:v + 1] = sorted(lst[j + 1:v + 1], key=lambda z: z[0])
#
#
# def make_list(dat):
#     lst = list()
#     for symbol in set(dat):
#         if symbol not in lst and symbol != ' ':
#             lst.append((symbol, str(round(dat.count(symbol) / len(''.join(dat.split())), 3))))
#     return lst
#
#
# text_file = open('text.txt')
# data = text_file.read().lower()
# text_file.close()
#
# print(f'\nContent of file text.txt:')
# print(data)
#
# syms_list = make_list(data)
# my_sort(syms_list)
#
# analysis_file = open('analysis.txt', 'w')
# for index, value in enumerate(syms_list):
#     analysis_file.write((value[0] + ' ' + value[1] + '\n'))
# analysis_file.close()
#
#
# analysis_file = open('analysis.txt')
# data_analysis = analysis_file.read()
# analysis_file.close()
#
# print(f'\nContent of file analysis.txt:')
# print(data_analysis)


# Task 9. War and world
#
# import collections
# import zipfile
#
#
# def unzip(archive):
#     zip_file = zipfile.ZipFile(archive, 'r')
#     for i_file_name in zip_file.namelist():
#         zip_file.extract(i_file_name)
#     zip_file.close()
#
#
# def collect_stats(name):
#     result = {}
#     if name.endswith('.zip'):
#         unzip(name)
#         name = ''.join((name[:-3], 'txt'))
#     text_file = open(name, 'r', encoding='utf-8')
#     for i_line in text_file:
#         for j_char in i_line:
#             if j_char.isalpha():
#                 if j_char not in result:
#                     result.setdefault(j_char, 0)
#                 result[j_char] += 1
#     text_file.close()
#     return result
#
#
# def print_stats(sts):
#     print("+{:-^19}+".format('+'))
#     print("|{: ^9}|{: ^9}|".format('word', 'frequency'))
#     print("+{:-^19}+".format('+'))
#     for char, count in sts.items():
#         print("|{: ^9}|{: ^9}|".format(char, count))
#     print("+{:-^19}+".format('+'))
#
#
# def sort_by_frequency(stats_dct):
#     sorted_values = sorted(stats_dct.values(), reverse=True)
#     sorted_dct = collections.OrderedDict()
#     for i_value in sorted_values:
#         for j_key in stats_dct.keys():
#             if stats_dct[j_key] == i_value:
#                 sorted_dct.setdefault(j_key, stats_dct[j_key])
#
#     return sorted_dct
#
#
# file_name = 'voina-i-mir.zip'
# stats = collect_stats(file_name)
# stats = sort_by_frequency(stats)
# print_stats(stats)
