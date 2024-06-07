# Task 1. Names
#
# summ, index_line = 0, 0
# try:
#     people_file = open('people.txt', 'r', encoding='utf-8')
#     for i_line in people_file:
#         length = len(i_line)
#         index_line += 1
#         if length < 4:
#             raise TypeError('Length of name must be more than 3 syms')
#         if i_line.endswith('\n'):
#             length -= 1
#         summ += length
#     people_file.close()
# except TypeError:
#     print('In line {}, name less than 3 symbols.'.format(index_line))
#     raise
# else:
#     print('Program completed without any errors.')


# Task 2. Logging
#
#
# def isPalindrome(string):
#     if len(string) < 2:
#         return True
#     elif string[0] == string[-1]:
#         return isPalindrome(string[1:-1])
#     else:
#         return False
#
#
# def add_to_errors_log(path, error):
#     path_file = open(path, 'a', encoding='utf-8')
#     path_file.write(error + '\n')
#     path_file.close()
#
#
# def format_row(line):
#     for char in line:
#         if char.isdigit():
#             raise ValueError('There is a digit in the line!')
#
#     if line.endswith('\n'):
#         line = line[:-1]
#     return line.replace(' ', '')
#
#
# words_count = 0
# words_file = open('words.txt', encoding='utf-8')
# for index, row in enumerate(words_file):
#     try:
#         row = format_row(row)
#         if isPalindrome(row.lower()):
#             words_count += 1
#     except ValueError:
#         error_name = f'ValueError: there is a digit in the line ({index + 1})!'
#         print(error_name)
#         add_to_errors_log('errors.log', error_name)
# words_file.close()
#
# print('Count palindromes:', words_count)
