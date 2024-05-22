# Task 1. Code review
#
# def my_func(dictionary):
#     total_len = 0
#     interests = list()
#     for i_key, i_val in dictionary.items():
#         interests.extend(i_val.get('interests', []))
#         total_len += len(i_val.get('surname', []))
#     return interests, total_len
#
#
# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
# pairs = [(key, val['age']) for key, val in students.items()]
# print('List of pairs (studentID - age): {}'.format(pairs))
#
# list_interests, total_family_len = my_func(students)
# print('\nList of interests - {interes}\nTotal length of surnames - {len}'.format(
#     interes=list_interests,
#     len=total_family_len
# ))


# Task 2. Universal programm 2
#
#
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# def find_elements(arr):
#     elements = list()
#     if isinstance(arr, list):
#         elements = [x for x in arr if is_prime(arr.index(x))]
#     elif isinstance(arr, str) or isinstance(arr, tuple):
#         for index, item in enumerate(arr):
#             if is_prime(index):
#                 elements.append(item)
#     return elements
#
#
# def main_func(arrange):
#     return find_elements(arrange)
#
# example1 = 'О Дивный Новый мир!'
# example2 = (100, 200, 300, 'буква', 0, 2, 'а')
#
# list_elements1 = main_func(example1)
# list_elements2 = main_func(example2)
#
# print(list_elements1)
# print(list_elements2)


