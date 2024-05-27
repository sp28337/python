# Task 1. Challenge
#
# def find_factorial(num):
#     if num == 1:
#         return 1
#     fact_n_minus_1 = find_factorial(num - 1)
#     return fact_n_minus_1 * num
#
#
# num_factorial = find_factorial(5)
# print(num_factorial)


# Task 2. Power of number
#
# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
#
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))


# Task 3. Seeking element
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def find_key(arr, key):
#     if key in arr:
#         return arr[key]
#     for sub_arr in arr.values():
#         if isinstance(sub_arr, dict):
#             val = find_key(sub_arr, key)
#             if val:
#                 break
#     else:
#         val = None
#     return val
#
#
# user_key = input('What key to find? ')
# result = find_key(site, user_key)
# print(result)
