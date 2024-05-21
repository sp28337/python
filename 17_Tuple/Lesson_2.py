# Task 1. Sabotage
#
# text = input('Enter the string: ')
# for index, sym in enumerate(text):
#     if sym == '~':
#         print(index, end=' ')


# Task 2. Dicts from lists
#
#
# import random, string
#
#
# def make_dict_from_list(some_list):
#     data_dict = dict()
#     for index, symbol in enumerate(some_list):
#         data_dict[index] = symbol
#     return data_dict
#
#
# alphabet = string.ascii_lowercase
# print(alphabet)
#
# list_1 = [random.choice(alphabet) for _ in range(10)]
# list_2 = [random.choice(alphabet) for _ in range(10)]
#
# print(f"First list: {list_1}\nSecond list {list_2}")
#
# dict1 = make_dict_from_list(list_1)
# dict2 = make_dict_from_list(list_2)
#
# print(f"\nFirst dict: {dict1}\nSecond dict: {dict2}")


# Task 3. Universal program
#
# def find_elements(arr):
#     elements = list()
#     if isinstance(arr, list):
#         elements = [x for x in arr if arr.index(x) % 2 == 0]
#     elif isinstance(arr, str) or isinstance(arr, tuple):
#         for index, item in enumerate(arr):
#             if index % 2 == 0:
#                 elements.append(item)
#     return elements
#
#
# example1 = 'О Дивный Новый мир!'
# example2 = (100, 200, 300, 'буква', 0, 2, 'а')
#
# list_elements1 = find_elements(example1)
# list_elements2 = find_elements(example2)
#
# print(list_elements1)
# print(list_elements2)
