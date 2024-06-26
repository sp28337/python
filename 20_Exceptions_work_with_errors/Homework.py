# Task 1. Names 2
#
#
# def find_total_length(path):
#     length = 0
#     with open(path, 'r', encoding='utf-8') as file:
#         for index, line in enumerate(file):
#             if line.endswith('\n'):
#                 line = line[:-1]
#             try:
#                 if len(line) < 3:
#                     raise ValueError(f'Error at line ({index + 1}). String must consist by 3 or more symbols.')
#             except ValueError:
#                 error = f'Error at line ({index + 1}). String must consist by 3 or more symbols.'
#                 write_err_to_log(error)
#                 print(error)
#             else:
#                 length += len(line)
#     return length
#
#
# def write_err_to_log(err):
#     with open('errors.log', 'a', encoding='utf-8') as file:
#         file.write(err + '\n')
#
#
# total_length = find_total_length('people.txt')
# print(total_length)


# Task 2. Coordinates
#
# import random
#
#
# def division_x_y(x, y):
#     try:
#         x += random.randint(0, 10)
#         y += random.randint(0, 5)
#         res = round((x / y), 2)
#         return res
#     except ZeroDivisionError:
#         return 0
#
#
# def division_y_x(x, y):
#     try:
#         x -= random.randint(0, 10)
#         y -= random.randint(0, 5)
#         res = round((y / x), 2)
#         return res
#     except ZeroDivisionError:
#         return 0
#
#
# try:
#     with open('coordinates.txt', 'r') as file:
#         for line in file:
#             nums_list = line.split()
#             res1 = division_x_y(int(nums_list[0]), int(nums_list[1]))
#             res2 = division_y_x(int(nums_list[0]), int(nums_list[1]))
#             number = random.randint(0, 100)
#             with open('result.txt', 'a') as file_2:
#                 my_list = sorted([str(res1), str(res2), str(number)])
#                 file_2.write(' '.join(my_list) + '\n')
#         else:
#             with open('result.txt', 'a') as file_2:
#                 file_2.write('\n')
#
# except FileNotFoundError:
#     print('Error. File not found!')


# # Task 3. Happy number
# import random
#
# summ = 0
# while summ < 777:
#     user_num = int(input('Enter random number: '))
#     summ += user_num
#     random_num = random.randint(1, 13)
#     try:
#         if random_num == 1:
#             raise Exception
#     except Exception:
#         print('Error, you are so unlucky!')
#         break
#     with open('numbers.log', 'a', encoding='utf-8') as numbers_file:
#         numbers_file.write(str(user_num) + '\n'


# Task 4. Registration
#
#
# def check_errors(string):
#     name, mail, age = string.split()
#     if len(string.split()) != 3:
#         raise ValueError
#     if not name.isalpha():
#         raise NameError
#     if not ('@' in mail and '.' in mail):
#         raise SyntaxError
#     if not 10 <= int(age) <= 99:
#         raise ValueError
#
#
# def check_file(path):
#     with open(path, 'r', encoding='utf-8') as file:
#         for line in file:
#             try:
#                 check_errors(line)
#             except ValueError:
#                 error = '<ValueError> Field age is not between 10 to 99'
#                 with open('registration_bad.log', 'a') as registration_bad_file:
#                     registration_bad_file.write(' - '.join((line[:-1], error)) + '\n')
#             except SyntaxError:
#                 error = '<SyntaxError> Field email does not contain <@> or <.>.'
#                 with open('registration_bad.log', 'a') as registration_bad_file:
#                     registration_bad_file.write(' - '.join((line[:-1], error)) + '\n')
#             except NameError:
#                 error = '<NameError> Name consists of not only letters.'
#                 with open('registration_bad.log', 'a') as registration_bad_file:
#                     registration_bad_file.write(' - '.join((line[:-1], error)) + '\n')
#             else:
#                 with open('registration_good.log', 'a') as registration_good_file:
#                     reg_good_file.write(line)
#
#
# path_to_file = 'registration.txt'
# check_file(path_to_file)
#
# print('Content of registration_good.log:')
# with open('registration_good.log', 'r') as reg_good_file:
#     data = reg_good_file.read()
#     print(data)
# print()
# print('Content of registration_bad.log:')
# with open('registration_bad.log', 'r') as reg_bad_file:
#     data = reg_bad_file.read()
#     print(data)


# Task 5. Text calculater
#
# def calc_func(lst, res=None):
#     try:
#         if len(lst) == 3:
#             if lst[1] == '+':
#                 res = int(lst[0]) + int(lst[2])
#             elif lst[1] == '-':
#                 res = int(lst[0]) - int(lst[2])
#             elif lst[1] == '*':
#                 res = int(lst[0]) * int(lst[2])
#             elif lst[1] == '/':
#                 res = int(lst[0]) / int(lst[2])
#             elif lst[1] == '//':
#                 res = int(lst[0]) // int(lst[2])
#             elif lst[1] == '%':
#                 res = int(lst[0]) % int(lst[2])
#             elif lst[1] == '**':
#                 res = int(lst[0]) ** int(lst[2])
#             else:
#                 raise KeyboardInterrupt
#         else:
#             raise ValueError
#     except ValueError:
#         res = 0
#     except KeyboardInterrupt:
#         res = 0
#     finally:
#         return res
#
#
# summ = 0
# path_to_file = 'calc.txt'
# with open(path_to_file, 'r', encoding='utf-8') as file:
#     for line in file:
#         result = calc_func(line.split())
#         summ += result
#
# print(summ)


# Task 6. Chat
#
# def main():
#     user_name = input('Enter user name: ')
#     while True:
#         try:
#             print('\nMENU\n[1] - Watch current chat\n[2] - Send a message\n')
#             user_action = input('Choose what to do: ')
#             if user_action in ('1', '[1]', 'one', 'first', 'f'):
#                 with open('chat.txt', 'r', encoding='utf-8') as file:
#                     chat_data = file.read()
#                     print(chat_data + '\n')
#             elif user_action in ('2', '[2]', 'two', 'second', 's'):
#                 message = input('Enter message: ')
#                 with open('chat.txt', 'a', encoding='utf-8') as file:
#                     file.write('{0} -> {1}\n'.format(user_name, message))
#             else:
#                 raise ValueError
#         except FileNotFoundError:
#             print('File not found.')
#         except ValueError:
#             print('Attention! <Incorrect type action>')
#
#
# main()


# Task 7. Text calculater 2
#
#
# def fix_function(*args):
#     print(f'Error was detected in the line <{' '.join(args)}>. Do you wanna fix? ', end='')
#     user_answer = input()
#     if user_answer in ('y', 'yes', 'ya', 'yah', 'ok', 'yess', 'yees', 'да', '1'):
#         fix_str = input('Enter fixed string: ')
#         fix_res = line_validation(*fix_str.split())
#     else:
#         fix_res = 0
#     return fix_res
#
#
# def do_operation(n1, operation, n2):
#     res = 0
#     if operation == '+':
#         res = n1 + n2
#     elif operation == '-':
#         res = n1 - n2
#     elif operation == '*':
#         res = n1 * n2
#     elif operation == '/':
#         res = n1 / n2
#     elif operation == '//':
#         res = n1 // n2
#     elif operation == '%':
#         res = n1 % n2
#     elif operation == '**':
#         res = n1 ** n2
#
#     return res
#
#
# def line_validation(*args):
#     try:
#         if len(args) == 3:
#             if ''.join((args[0], args[2])).isdigit():
#                 if args[1] in ('+', '-', '*', '**', '/', '//', '%'):
#                     result = do_operation(int(args[0]), args[1], int(args[2]))
#                 else:
#                     raise ValueError
#             else:
#                 raise TypeError
#         else:
#             raise IndexError
#
#     except (IndexError, TypeError, ValueError):
#         result = fix_function(*args)
#     return result
#
#
# summ = 0
# path_to_file = 'calc.txt'
# with open(path_to_file, 'r', encoding='utf-8') as file:
#     for line in file:
#         res = line_validation(*line.split())
#         summ += res
#
# print(summ)
