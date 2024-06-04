# Task 1. Summ of numbers
#
# count_nums_lst = [str(x) for x in range(1, int(input('How much numbers will be in file? ')) + 1)]
# numbers = open('numbers.txt', 'w')
# numbers.write('\n'.join(count_nums_lst))
#
# #               or
# # count_nums = int(input('How much numbers will be in file? '))
# # for i_num in range(1, count_nums + 1):
# #     numbers.write(str(i_num) + '\n')
# numbers.close()
#
# print('Content of numbers.txt:')
# numbers = open('numbers.txt', 'r')
# summ = 0
# for i in numbers:
#     print(i, end='')
#     summ += int(i)
#
# numbers.close()
#
# print()
# print('Content of answer.txt:')
# answer = open('answer.txt', 'w')
# answer.write(str(summ))
# answer.close()
#
# answer = open('answer.txt', 'r')
# data = answer.read()
# print(data)
# answer.close()


# Task 2. All in one
#
# import os
# abs_path = os.path.abspath(os.path.join('..', '1_condition'))
#
# scripts_file = open('scripts.txt', 'w')
# for i_elem in os.listdir(abs_path):
#     if os.path.isfile(os.path.join(abs_path, i_elem)):
#         i_elem_open = open(os.path.join(abs_path, i_elem), 'r')
#         f_data = i_elem_open.read()
#         scripts_file.write(f_data + '*' * 40 + '\n\n')
#         i_elem_open.close()
# scripts_file.close()
#
#
# scripts_file = open('scripts.txt')
# data = scripts_file.read()
# print(data)
# scripts_file.close()
