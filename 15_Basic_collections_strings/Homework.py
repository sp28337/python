# Task 1. Restaurant's menu
#
# while True:
#     menu = input('Available menu: ')
#     if ';' in menu:
#         break
#     else:
#         print('Error: dishes must be separated by ;')
#
# print('At the moment we have:', menu.replace(';', ', '))


# Task 2. Longest word
#
# text = input('Enter text: ')
# list_words = text.split()
# last_word = list_words[0]
#
# for word in list_words:
#     if len(word) > len(last_word):
#         last_word = word
#
# print(last_word, len(last_word))


# Task 3. Files
#
# file_name = input('Enter file name: ')
# # forbidden_syms = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
# if (file_name.startswith('@') or
#     file_name.startswith('№') or
#     file_name.startswith('$') or
#     file_name.startswith('%') or
#     file_name.startswith('^') or
#     file_name.startswith('&') or
#     file_name.startswith('*') or
#     file_name.startswith('(') or
#     file_name.startswith(')')):
#     print('Error: name starts with one of forbidden symbols.')
# else:
#     if file_name.endswith('.txt') or file_name.endswith('.docx'):
#         print('Correct file name.')
#     else:
#         print('Error: wrong decoding file. Expected .txt or .docx')


# Task 4. Upper letters
#
# text = input('Enter the string: ')
# print(text.title())


# Task 5. Capitan Flint
#
# y_path = input('Enter path OY: ')
# x_path = input('Enter path OX: ')
# x = y = 0
# x_digits = [x for x in x_path if x.isdigit()]
# y_digits = [y for y in y_path if y.isdigit()]
#
#
# if x_path.startswith('East'):
#     x = int(''.join(x_digits))
# elif x_path.startswith('West'):
#     x = 0 - int(''.join(x_digits))
#
# if y_path.startswith('South'):
#     y = 0 - int(''.join(y_digits))
# elif y_path.startswith('North'):
#     y = int(''.join(y_digits))
#
# print('Coordinates: {x_o} {y_o}'.format(x_o=x, y_o=y))


# Task 6. Password
#
# def is_three_digits(string):
#     nums = 0
#     for sym in string:
#         if sym.isdigit():
#             nums += 1
#     if nums >= 3:
#         return True
#     return False
#
#
# def is_upper_symbol(string):
#     flag = False
#     for sym in string:
#         if sym.isupper():
#             flag = True
#             break
#     return flag
#
#
# while True:
#     password = input('Enter password: ')
#     if len(password) >= 8 and is_three_digits(password) and is_upper_symbol(password):
#         print('Strong password!')
#         break
#     else:
#         print('Password must contain at least 8 symbols, 3 digits and 1 uppercase character. Try again.')