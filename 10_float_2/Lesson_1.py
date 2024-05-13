# def summa_n(n):
#     summ = 0
#     for i in range(1, n + 1):
#         summ += i
#     return summ
#
#
# number = int(input('Enter the number: '))
# summ_1 = summa_n(number)
# summ_2 = summa_n(summ_1)
# print(summ_1, summ_2)


# def gcb(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     gcb = a + b
#     return gcb
#
#
# number_1 = int(input('Enter number 1: '))
# number_2 = int(input('Enter number 2: '))
#
# gcd = gcb(number_1, number_2)
# print(gcd)


# def numeral_count(t):
#     first_task = 0
#     for i in range(t):
#         numbers = int(input('Enter number: '))
#         if numbers < 0:
#             continue
#         elif numbers > first_task:
#             first_task = numbers
#     return first_task
#
#
# task_numbers = int(input('Enter how many tasks will be: '))
# priority_task = numeral_count(task_numbers)
# print(priority_task)
