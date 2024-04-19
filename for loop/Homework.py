# numbers = [114, 12, 14, 10605, 4907, 450]
# for I in numbers:
#     if i % 2 == 0 and i % 3 != 0:
#         print(i, 'number is correct!')
#     else:
#         print(i, 'number is not correct')


# count = 0
# for i in range(10):
#     num = int(input('Enter a number: '))
#     if num > 0 and num % 2 == 0:
#         count += 1
# print(count)


# summ = 0
# for i in range(12):
#     salary = int(input('Enter your salary: '))
#     summ += salary
# print('Salary for 12 months =', summ)


# pings = int(input('How much pings? '))
# for i in range(pings):
#     print('   _~_    ')
#     print('  (o o)   ')
#     print(' /  V  \  ')
#     print('/(  _  )\ ')
#     print('  ^^ ^^   ')


# violations = 0
# for i in range(30, 36):
#     people = int(input(f'How much people at sector {i}? '))
#     if people > 10:
#         print('People are more than need!')
#         violations += 1
#     else:
#         print('All is right')
# print('Total violations: ', violations)


# poin_a = int(input('Beginning of the segment: '))
# poin_b = int(input('End of the segment: '))
# for i in range(poin_a, poin_b + 1):
#     y = i ** 3 + 2 * i ** 2 - 4 * i + 1
#     print(f'In point {i} function = {y}')


# n = int(input('Enter number: '))
# for i in range(100, 1000):
#     if i % 10 + (i // 10) % 10 + i // 100 == n:
#         print(f'Summ digits of number {i} = {n}')


# num = int(input('Enter number: '))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)


# people = int(input('How much people in the class? '))
# good, middle, bad = 0, 0, 0
# for i in range(people):
#     mark = int(input('What is the mark? '))
#     if mark == 5:
#         good += 1
#     elif mark == 4:
#         middle += 1
#     elif mark == 3:
#         bad += 1
#     else:
#         print('Wrong mark')
# if good > middle and good > bad:
#     print('Good mark more then others!')
# elif middle > bad and middle > good:
#     print('Middle mark more then others!')
# elif bad > middle and bad > good:
#     print('Bad mark more then others!')


# a = int(input('Enter first num: '))
# b = int(input('Enter second num: '))
# count = 0
# summ = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         count += 1
#         summ += i
# print(f'Average = {summ // count}')


# bacterias = int(input('Enter count of bacterias: '))
# a_temp = int(input('Enter a_temperature: '))
# b_temp = int(input('Enter b_temperature: '))
# c_temp = int(input('Enter c_temperature: '))
# d_temp = int(input('Enter d_temperature: '))
# probe_1, probe_2 = bacterias, bacterias
# for i in range(a_temp, b_temp + 1):
#     probe_1 *= i
# for i in range(c_temp, d_temp + 1):
#     probe_2 *= i
# difference = abs(probe_1 - probe_2)
# print(f'Population in first probe: {probe_1}')
# print(f'Population in second probe: {probe_2}')
# print(f'Difference is {difference}')


# for i in range(10, 100):
#     a = ((i % 10) * (i // 10)) * 3
#     if a == i:
#         print(a)


# import time
# t0 = time.time()
# steps = int(input('Count of steps: '))
# for i in range(1, steps + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# t1 = time.time()
# total = t1 -t0
# print(total)
#
# t2 = time.time()
# n = int(input('Enter the steps: '))
# s = ''
# for i in range(1, n + 1):
#     s += str(i)
#     print(s)
# t3 = time.time()
# total2 = t3 - t2
# print(total2)


# last_salary = 0
# for i in range(10):
#     salary = int(input('Enter your salary: '))
#     if salary <= last_salary:
#         print('Salary is not increasing')
#     else:
#         print('Salary is increasing')
#     last_salary = salary


# card_num = int(input('How much cards numbers? '))
# summ = 0
# for i in range(1, card_num + 1):
#     summ += i
# for j in range(card_num - 1):
#     last_card = int(input('Enter the last card: '))
#     summ -= last_card
# print(summ)