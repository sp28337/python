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
