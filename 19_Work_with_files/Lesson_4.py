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

