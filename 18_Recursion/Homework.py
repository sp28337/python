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


# Task 4. Seeking exemplar 2
#
# def find_key(dct, key, deep=10):
#     if deep == 0:
#         result = 'Max depth'
#         return result
#     if key in dct:
#         return dct[key]
#     for item in dct.values():
#         if isinstance(item, dict):
#             result = find_key(item, key, deep - 1)
#             if result:
#                 break
#     else:
#         result = 'There are not key like that.'
#         return result
#     return result
#
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
# key_to_find = input('What key do you wanna find? ')
# ask_for_deep = input('Do you wanna set max depth(10 - default)? ')
#
# if ask_for_deep in ('yes', 'yep', 'y', 'ya'):
#     size_depth = int(input('Enter depth size: '))
#     res = find_key(site, key_to_find, deep=size_depth)
#     print(res)
# else:
#     res = find_key(site, key_to_find)
#     print(res)


# Task 5.


# Task 6. Deep copying
#
# def make_site(name):
#     site = {
#         'html': {
#             'head': {
#                 'title': 'Куплю/продам {} недорого'.format(name)
#             },
#             'body': {
#                 'h2': 'У нас самая низкая цена на {}'.format(name),
#                 'div': 'Купить',
#                 'p': 'Продать'
#             }
#         }
#     }
#     return site
#
#
# number_of_sites = int(input('Enter numbers of sites: '))
# for _ in range(number_of_sites):
#     product_name = input('\nEnter product name for new site: ')
#     result = make_site(product_name)
#     print(f'\nSite for {product_name}:')
#     print(result)


# Task 7. Advanced sum function
#
# def my_sum(*args):
#     total = 0
#     for i_arg in args:
#         if isinstance(i_arg, list):
#             total += my_sum(*i_arg)
#         else:
#             total += i_arg
#     return total
#
#
# result = my_sum([[1, 2, [3]], [1], 3])
# print(result)


