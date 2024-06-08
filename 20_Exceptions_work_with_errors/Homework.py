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
