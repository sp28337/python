# Task 1. Endless generator
#
# def endless_gen():
#     counter = 0
#     while True:
#         yield counter
#         counter += 1
#
#
# gen = endless_gen()
# for i in gen:
#     print(i)


# Task 2. Very big file
#
# def my_gen(limit):
#     for i in range(limit.split):
#         yield str(i)
#
#
# with open('numbers.txt', 'w', encoding='utf-8') as file:
#     for i in range(0, 100000, 10):
#         file.write(' '.join((str(x) for x in range(i, i + 11))) + '\n')
#
#
# def find_summ_nums(path):
#     with open(path, 'r', encoding='utf-8') as file_r:
#         for line in file_r:
#             for number in line.split():
#                 yield int(number)
#
#
# def sum_large_file(path_f):
#     total_sum = 0
#     for number in find_summ_nums(path_f):
#         total_sum += number
#     return total_sum
#
#
# path_file = 'numbers.txt'
# print(sum_large_file(path_file))
