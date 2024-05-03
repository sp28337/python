# def float_x(x):
#     if x < 0:
#         print('Number must be more than zero!')
#
#     power = 0
#     copy_x = x
#     if x < 1:
#         while x < 1:
#             x *= 10
#             power -= 1
#         print(f"Float format: x = {round(x, 1)} * 10 ** {power}")
#     else:
#         while copy_x > 0:
#             copy_x //= 10
#             power += 1
#         copy_x = x * 10 ** -(power - 1)
#         print(f"Float format: x = {copy_x} * 10 ** {power - 1}")
#
#
# number = float(input('Enter the number: '))
# float_x(number)


# def get_parent_names_total_length(x, y):
#     count_x = 0
#     count_y = 0
#     for i in x:
#         count_x += 1
#     for j in y:
#         count_y += 1
#     summ = count_x + count_y
#     print(f"Symbols in father's name: {count_x}\nSymbols in mather's name: {count_y}\nSumma: {summ}")
#
#
#
# father = input('Enter name your father: ')
# mather = input('Enter name your mather: ')
# get_parent_names_total_length(father, mather)


# def maximum(a, b ,c):
#     max1 = (abs(a - b) + (a + b)) // 2
#     max2 = (abs(max1 - c) + (max1 + c)) // 2
#     print(max2)
#
# num1 = int(input('Enter the number 1: '))
# num2 = int(input('Enter the number 2: '))
# num3 = int(input('Enter the number 3: '))
#
# maximum(num1, num2, num3)


# num1 = input('Enter the number 1: ')
# num2 = input('Enter the number 2: ')
#
# print(f"First number {num1[::-1]}\nSecond number {num2[::-1]}")
# summ = int(num1[::-1]) + int(num2[::-1])
# print('Summa:', summ, '\nReversed summ:', int(num2) + int(num1))


# text = input('Enter exponential form of a number: ')
# mantissa = ''
# power = ''
# for i in text:
#     if i == 'e':
#         print(f"Mantissa of number ({text}) is {mantissa}", end=' ')
#         power = ''
#         continue
#     mantissa += i
#     power += i
# print(f"power of number ({text}) is {power}")


# import math
#
# result = 0
# i = 0
# add_m = 1
# while add_m > 1e-2:
#     add_m = 1 / math.factorial(i)
#     result += add_m
#     i += 1
# print(result)
# print(math.e)


# def rover_control(x, y):
#     print(f"Rover at point {x} : {y}", end=' ')
#     answer = input('Enter command:\n')
#     if answer == 'w':
#         y += 1
#     elif answer == 's':
#         y -= 1
#     elif answer == 'a':
#         x -= 1
#     elif answer == 'd':
#         x += 1
#     rover_control(x, y)
#
#
# x = 0.001 * 1.496e11
# y = 0
#
# rover_control(x,y)


# def num_rev(n):
#     counter = 0
#     copy_n = n
#     while copy_n > 0:
#         counter += 1
#         copy_n = copy_n // 10
#     if counter < 3:
#         return 0
#     else:
#         last_digit = n % 10
#         first_digit = n // 10 ** (counter - 1)
#         between_digits = n % 10 ** (counter - 1) // 10
#         n = last_digit * 10 ** (counter - 1) + between_digits * 10 + first_digit
#         return n
#
#
# first_n = int(input("Введите первое число: "))
# second_n = int(input("Введите второе число: "))
# num1 = num_rev(first_n)
# num2 = num_rev(second_n)
# print(num1, num2)
# print(num1 + num2)


# def power(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * power(a, n - 1)
#
#
# a_num = float(input('Enter a number: '))
# n_num = float(input('Enter n number: '))
#
# print(power(a_num, n_num))


# def count_ampl(a, b):
#     counter = 0
#     while a > b:
#         a -= (a * 8.4) / 100
#         counter += 1
#     return counter
#
#
# start_amplitude = int(input('Enter start amplitude: '))
# end_amplitude = float(input('Enter end amplitude: '))
# coleb = count_ampl(start_amplitude, end_amplitude)
# print(f"Coleb {coleb}")


# d_from, d_to = 0, 4
# max_danger = float(input('Enter max danger level: '))
# x = d_from + (d_to - d_from) / 2
# d = x ** 3 - 3 * x ** 2 - 12 * x + 10
# if max_danger < 0:
#     print('Error!')
# else:
#     print(x, d)
#     while abs(d) > max_danger:
#         if d < 0:
#             d_to = x
#         else:
#             d_from = x
#         x = d_from + (d_to - d_from) / 2
#         d = x ** 3 - 3 * x ** 2 - 12 * x + 10
#         print(x, d)
#
# print(x)


# def sum_of_series(precision, x):
#     previous = i = 0
#     current = fn = xn = 1
#     while abs(current - previous) > precision:
#         previous = current
#         xn *= x * x
#         i += 1
#         fn *= 2 * i * (2 * i - 1)
#         current += (-1 if i % 2 else 1) * xn / fn
#     return current
#
# print('Summa =', sum_of_series(float(input('Enter precision: ')), float(input('Enter x: '))))


# s = float(input('Enter credit summ: '))
# n = int(input('For how many years? '))
# i = int(input('How many percent? '))
#
# k = i * ((1 + i) ** n) / (1 + i) ** n - 1
# a = round(k * s, 2)
# print(k * ((s * i) / 100), (a * i) / 100, s, (s * i) / 100)