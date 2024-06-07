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
