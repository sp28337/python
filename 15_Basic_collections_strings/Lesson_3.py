# Task 1. Ceasar cipher 2
#
# def caesar_cipher(string, user_shift):
#     char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in string.lower()]
#     return ''.join(char_list)
#
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# input_str = input('Enter message to encode: ')
# shift = int(input('Enter shift: '))
#
# output_str = caesar_cipher(input_str, shift)
#
# print(output_str)


# Task 2. Path to file
#
# path_to_file = input('Enter path to file: ')
# disk = input('On which disk should the file be located: ')
# extension = input('Required file extension: ')
# if path_to_file.startswith(disk) and path_to_file.endswith(extension):
#     print('Path is correct!')
# else:
#     print('Error')