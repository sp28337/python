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


# Task 3. Function
#
# import random
#
#
# def some_func(arr_tuple, rand_elem):
#     my_data = list()
#     if arr_tuple.count(rand_elem) == 1:
#         for index in arr_tuple[arr_tuple.index(rand_elem):]:
#             my_data.append(index)
#         return tuple(my_data)
#     elif arr_tuple.count(rand_elem) > 1:
#         my_data.append(rand_elem)
#         for index in arr_tuple[arr_tuple.index(rand_elem) + 1:]:
#             if index == rand_elem:
#                 my_data.append(index)
#                 return tuple(my_data)
#             my_data.append(index)
#     else:
#         return tuple()
#
#
# new_tuple = tuple(random.randint(0, 10) for _ in range(10))
# elem = random.randint(0, 10)#int(input('Enter random number: '))
#
# print(new_tuple, elem)
#
# another_tuple = some_func(new_tuple, elem)
#
# print(another_tuple)


# Task 4. Players
#
# players = {
#     ("Ivan", "Volkin"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }
#
# new_data = [key + val for key, val in players.items()]
# print(new_data)


# Task 5. One family
#
# family_dict = {
#     ("Tarakanova", "Kristina"): 25,
#     ("Tarakanov", "Pavel"): 29,
#     ("Saxarov", "Andrey"): 52,
#     ("Pavlov", "Ivan"): 30
# }
#
#
# surname = input('Enter surname: ').title()
#
# found = False
# for key, val in family_dict.items():
#     if key[0].startswith(surname[:5]):
#         print(f"{' '.join([key[0], key[1]])} {val}")
#         found = True
#
# if not found:
#     print('No matching surnames found.')


# Task 6. By pairs
#
# origin_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# new_list, index_lst = list(), list()
#
# for i in origin_list:
#
#     if len(index_lst) >= 2:
#         new_list.append(tuple(index_lst))
#         index_lst = list()
#         index_lst.append(i)
#     else:
#         index_lst.append(i)
#
# else:
#     if len(index_lst) == 2:
#         new_list.append(tuple(index_lst))
#     else:
#         new_list.extend(tuple(index_lst))
#
# print(new_list)
#
# new_list = [(val, origin_list[index + 1])
#             for index, val in enumerate(origin_list)
#             if not val == origin_list[-1] and index % 2 == 0]
#
# print(new_list)


# Task 7. Sorted function
#
# import random
#
#
# def sorted_tuple(some_tuple):
#     if all(isinstance(i, int) for i in some_tuple):
#         return tuple(sorted(some_tuple))
#     else:
#         return some_tuple
#
#
# my_tuple = tuple(random.randint(0, 100) for _ in range(10))
# print(my_tuple)
#
# my_sorted_tuple = sorted_tuple(my_tuple)
# print(my_sorted_tuple)


# Task. 8 Contacts 3
#
# def add_contact(contacts):
#     surname_name = tuple(input('Enter surname and name of the contact: ').title().split())
#     if surname_name in contacts:
#         print('This contact already exists')
#     else:
#         phone = int(input('Enter phone number of the contact: '))
#         contacts[surname_name] = phone
#     print('\nPHONE BOOK:')
#     for key, val in contacts.items():
#         print('{0} {1} --- {2}'.format(key[0], key[1], val))
#     print()
#
#
# def find_contact(contacts):
#     find_to = input('Enter person to find: ').title()
#     for k, v in contacts.items():
#         if find_to in k:
#             print(f"Number of {find_to} is {v}")
#             break
#     else:
#         print('There are not contact like this in your phonebook')
#     print()
#
#
# def main_menu(contacts):
#
#     while True:
#         print('What do you want to do?\n1 - ADD CONTACT\n2 - FIND PERSON IN CONTACT LIST')
#         answer = int(input(''))
#         if answer == 1:
#             add_contact(contacts)
#         elif answer == 2:
#             find_contact(contacts)
#
#
# contacts_book = {('Pavel', 'Tarakanov'): 89307407771}
# main_menu(contacts_book)
