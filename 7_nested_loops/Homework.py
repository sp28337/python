# for i in range(6):
#     for j in range(6):
#         print(i + j * 2, end='\t')
#     print()


# for i in range(1, 6):
#     for j in range(1, 6):
#         if j <= i:
#             print(i, end='\t')
#     print()


# for i in range(20):
#     for j in range(50):
#         if i == 0 and j == 24:
#             print('^', end='')
#         elif i == 9 and j == 24:
#             print('+', end='')
#         elif j == 49 and i == 9:
#             print('>', end='')
#         elif j == 24:
#             print('|', end='')
#         elif i == 9:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()


# height = int(input('Enter height: '))
# weight = int(input('Enter weight: '))
# for i in range(height):
#     if i == 0 or i == height - 1:
#         print('|' + '-' * weight + '|', end='')
#     else:
#         print('|' + ' ' * weight + '|', end='')
#     print()


# size = int(input('Enter size: '))
# for i in range(size + 1):
#     for j in range(size + 1):
#         if i == j or size - i == j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()


# import math
# number = int(input('Enter number: '))
# prime = True
# for j in range(2, int(math.sqrt(number))):
#     if number % j == 0:
#         prime = False
#         break
# if prime:
#     print('Prime')
# else:
#     print('Composite')


# size_matrix = int(input('Enter matrix size: '))               #??????????????
# for i in range(size_matrix):
#     for j in range(size_matrix):
#         if i == j or j + i == size_matrix - 1:
#             print(1, end=' ')
#         else:
#             print(0, end=' ')
#     print()


# start = int(input('Enter start: '))
# finish = int(input('Enter finish: '))
# for i in range(start, finish + 1):
#     print('->', end=' ')
#     while i != 1:
#         print(i, end=' ')
#         if i % 2 == 0:
#             i //= 2
#         elif i % 2 != 0:
#             i = (i * 3 + 1) // 2
#     print(1, end='\n')


# summ = 0
# factorial = 1
# number = int(input('Enter the number: '))
# for i in range(1, number + 1):
#     factorial *= i
#     summ += factorial
# print(summ)


# total_num = int(input('How many numbers will there be? '))
# last_num, max_summ, summ = 0, 0, 0
# for i in range(total_num):
#     number = int(input('Enter the number: '))
#     last_num = number
#
#     if number > 0:
#         while number > 0:
#             summ += number % 10
#             number //= 10
#         if summ > max_summ:
#             max_summ = summ
#             m_n = last_num
#             summ = 0
# print(m_n, max_summ)


# summ = 0
# for i in range(1, 10001):
#     for j in range(1, i):
#         if i % j == 0:
#             summ += j
#     if summ == i:
#         print(i)
#     summ = 0


# name = input('Enter your name: ')
# for i in range(3):
#     if i == 1:
#         print('| ' + name + ' |')
#     else:
#         print('|-' + '-' * len(name) + '-|')


# pyramid_height = int(input('What is the height of the pyramid? '))
# for i in range(1, pyramid_height + 1):
#     print(' ' * (pyramid_height - i) + '#' * (i * 2 - 1))


# k = 1
# levels = int(input('How much levels will there be? '))
# for i in range(1, levels + 1):
#     print('   ' * (levels - i), end='')
#     for j in range(i):
#         print(k, end='    ')
#         k += 2
#     print()


# number = int(input('Enter the number: '))
# for i in range(number):
#     for j in range(i + 1):
#         print(number - j, end="")
#     print(('.' * (number - i - 1)) * 2, end='')
#     for k in range(i, -1, -1):
#         print(number - k, end="")
#     print()


# summ = 1
# triangle_size = int(input('What is the size of the triangle? '))              #??????????????
# for i in range(1, triangle_size + 1):
#     print(' ' * (triangle_size - i), end='')
#     for j in range(1, i + 1):
#         if i == j or j == 1:
#             print(1, end=' ')
#         else:
#             print(j, end=' ')
#     print()