# Task 1. Challenge 2
#
# def seq_num(num):
#     if num == 0:
#         return 1
#     seq_num(num - 1)
#     print(num)
#
#
# number = int(input('Enter the number: '))
# seq_num(number)


# Task 2. My own zip 2
#
# def clone_zip(*iterables):
#     length = min(len(item) for item in iterables)
#     tpl = (tuple(elem[index] for elem in map(tuple, iterables))
#            for index in range(length))
#     return tpl
#
#
# a = (10, 20, 30, 40, 50)
# b = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55}
# c = 'abc'
# e = {111, 222, 333, 444}
#
# print(*zip(a, b, c, e))
#
# result = clone_zip(a, b, c, e)
#
# print(*result)


# Task 3. Fibonacci numbers
#
# def find_num_position_fibonacci(number):
#     if number <= 1:
#         return number
#     else:
#         return find_num_position_fibonacci(number - 1) + find_num_position_fibonacci(number - 2)
#
#
# num = int(input())
# print(num, find_num_position_fibonacci(num))

