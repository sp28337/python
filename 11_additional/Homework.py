# def summa_from_1_to(n):
#     summa = 0
#     while n > 0:
#         summa += n % 10
#         n //= 10
#     return summa
#
#
# def count_numbers(n):
#     count_n = 0
#     while n > 0:
#         count_n += 1
#         n //= 10
#     return count_n
#
#
# number = int(input('Enter the number: '))
# x = summa_from_1_to(number)
# y = count_numbers(number)
# print(f"Summa digits: {x}\nCount of digits in the number: {y}\nDifference of summa and count: {x - y}")


# def rev_float(n):
#     integer_n1 = int(n)
#     float_n1 = int(round(n - integer_n1, 2) * 100)
#     counter_int = 0
#     int_n1_copy = integer_n1
#     while int_n1_copy > 0:
#         counter_int += 1
#         int_n1_copy //= 10
#
#     first_n_int = integer_n1 // 10 ** (counter_int - 1)
#     last_n_int = integer_n1 % 10
#     middle_int = integer_n1 - first_n_int * 10 ** (counter_int - 1) - last_n_int
#
#     first_n_float = float_n1 // 10
#     last_n_float = float_n1 % 10
#
#     rev_int_n1 = last_n_int * 10 ** (counter_int - 1) + middle_int + first_n_int
#     rev_float_n1 = (last_n_float * 10 + first_n_float) / 100
#
#     first_rev_num = rev_int_n1 + rev_float_n1
#     return first_rev_num
#
#
# n1 = float(input('Enter number 1: '))
# n2 = float(input('Enter number 2: '))
#
# rev_n1 = rev_float(n1)
# rev_n2 = rev_float(n2)
#
# print(f"First number reversed: {rev_n1}\nSecond number reversed: {rev_n2}\nSumma: {rev_n1 + rev_n2}")


# def smallest_divider(n):
#     for i in range(2, n + 1):
#         if n % i == 0:
#             return i
#
#
# number = int(input('Enter the number: '))
# small_divider = smallest_divider(number)
# print('Наименьший делитель, отличный от единицы:', small_divider)


# import math
#
#
# def check_point(x, y, r):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     if distance <= radius:
#         print('Point is nearby')
#     else:
#         print('Point is not here')
#
#
# x1 = float(input('Enter X coordinate: '))
# y1 = float(input('Enter Y coordinate: '))
# radius = float(input('Enter radius: '))
# check_point(x1, y1, radius)


# first_year = int(input('Enter first year: '))
# second_year = int(input('Enter second year: '))
# for i in range(first_year, second_year + 1):
#     for j in str(i):
#         if str(i).count(j) >= 3:
#             print(i)
#             break

