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


# Task 7. Digits in the string
#
# def find_digits(string):
#     nums = []
#     for sym in string:
#         if sym.isdigit():
#             nums.append(sym)
#     return ''.join(nums)
#
#
# text = input('Enter a string: ')
#
# digits = find_digits(text)
# print('Numbers:', digits)


# Task 8. Compression
#
# def comprehension_func(string):
#     copmr_str = ''
#     counter = 1
#     sym2 = string[0]
#     for sym1 in range(len(string)):
#         if string[sym1] == sym2:
#             counter += 1
#         else:
#             copmr_str += sym2 + str(counter)
#             sym2 = string[sym1]
#             counter = 1
#     copmr_str += sym2 + str(counter)
#     return copmr_str
#
#
# text = input('Enter message to encode: ')
#
# encoded_str = comprehension_func(text)
# print('Encoded string:', encoded_str)


# Task 9. IP - address 2
#
# def is_correct_ip(ip):
#
#     if len(ip) == 4:
#         for i in range(len(ip)):
#             if not ip[i].isdigit():
#                 return print(ip[i], '- not an integer')
#
#             elif not 0 <= int(ip[i]) <= 255:
#                 return print(f"{ip[i]} must be between 0 and 255")
#
#         else:
#             return print('IP - address is correct')
#     else:
#         return print('Address - 4 digits, separated by dots.')
#
#
# ip_address = input('Enter IP: ').split()
# is_correct_ip(ip_address)


# Task 10. Mathematic
#
#
# equation = '(5+4)*2-10'
# print(eval(equation))