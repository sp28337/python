# months = 0
# for i in range(100 - 4, 0, -4):
#     months += 1
#     print(f"In {months} months you will have {i} kg of food")


# summ = 0
# n = int(input('Enter number of range: '))
# for i in range(1, n // 2 + 1):
#     summ += (i * 2) - 1
# print(summ)


# summ = 0
# debtors = int(input('Enter the number of debtors: '))
# for i in range(0, debtors + 1, 5):
#     print(f"Debtor number {i}")
#     debt = int(input('How much do you owe? '))
#     summ += debt
# print('Total summa of debts is', summ)


# seconds = int(input('How many seconds left? '))
# for i in range(seconds, -1, -1):
#     fix = int(input('Do you wanna cansel boom? '))
#     print(f"Seconds to boom {i}")
#     if i == 0:
#         print('The bomb exploded!')
#         break
#     elif not fix:
#         continue
#     else:
#         print(f'The bomb was defused.\nTill explosion left {i} seconds')
#         break


# duged_up = int(input('How much already was dig up? '))
# meters = int(input('How many meters apart are potatoes planted? '))
# potatoes = 0
# for i in range(duged_up, 101, meters):
#     potatoes += 3
# print(f"Total potato tubers: {potatoes}")


# summ_trees = 0
# age_tree = int(input('Enter age of tree: '))
# girl_age = 6
# k = int(input('After how many years should trees be planted? '))
# while girl_age <= age_tree:
#     planted_tree = int(input('How many trees should be planted? '))
#     summ_trees += planted_tree
#     girl_age += k
# print(f"Total summa of trees were planted: {summ_trees}")


# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# c = int(input('Enter number: '))
# count = 0
# summ = 0
# for i in range(a, b):
#     if i % c == 0:
#         count += 1
#         summ += i
# print(f"Average of {summ} = {summ // count}")


# start = int(input('Start: '))
# finish = int(input('Finish: '))
# step = int(input('Step: '))
# for i in range(finish, start - 1, step):
#     y = i ** 3 + (2 * i ** 2) - 4 * i + 1
#     print(f"In point {i} function is {y}")


# square = 12
# letter = int(input('Letter size: '))
# count = 0
# while letter > square:
#     letter //= 2
#     count += 1
# print(f"You need to fold the letter {count * 2} time(s)")


# monthly_grant = int(input('Enter your monthly educational grant: '))
# expenses = int(input('Expenses per month is: '))
# summ = 0
# for i in range(1, 11):
#     summ += expenses
#     expenses += 3 * expenses // 100
# money = monthly_grant * 10 - summ
# if money < 0:
#     print(f"Need ask parents for {money * -1} dollars")
# else:
#     print('You do not need ask for money')


# s = 1
# n = int(input('Enter the n: '))
# for i in range(1, n + 1):
#     s += ((-1) ** i) * (1 / (2 ** i))
# print(f"Summa of arithmetic progressy is {s} ")


# import time
# t_1 = time.time()
# numerator = 1
# devider = 1
# k = 1
# x = int(input('Enter X: '))
# while k < 64:
#     numerator *= x - k
#     k = k * 2 + 1
# k = 2
# while k < 65:
#     devider *= x - k
#     k *= 2
# print(round(numerator / devider, 2))
# t_2 = time.time()
# time = t_2 - t_1
# print(time)


# a = int(input('Enter A number: '))
# b = int(input('Enter B number: '))
# c = int(input('Enter C number: '))
# d = int(input('Enter D number: '))
# if 0 <= c <= d and a > 0 and b > 0 and c > 0 and d > 0:
#     for i in range(a, b + 1):
#         if i % d != 0:
#             print(i)
# else:
#     print(f"Number {c} must be equal or between 0 and {d}, and all numbers must be positive.")


# boys = int(input('How much boys? '))
# girls = int(input('How much girls? '))
# answer = ''
# if boys > girls * 2 or girls > boys * 2:
#     print('Error!')
# elif boys >= girls:
#     k = boys - girls
#     for bgb in range(k):
#         answer += 'BGB'
#     for bg in range(girls - k):
#         answer += 'BG'
# else:
#     k = girls - boys
#     for gbg in range(k):
#         answer += 'GBG'
#     for gb in range(boys - k):
#         answer += 'GB'
# print(answer)

