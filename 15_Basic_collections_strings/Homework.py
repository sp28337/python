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


