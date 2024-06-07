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
