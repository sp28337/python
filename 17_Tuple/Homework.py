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


# Task 9. Competition protocol


#def tuple_gamers(string):
#
#
#
#
# game_protocol = list()
# list_winners = list()
#
# entries = int(input('How many entries are included in the protocol?: '))
#
# for entry in range(entries):
#     print(f'{entry + 1} entry:', end=' ')
#     input_data = input('').split()
#     game_protocol.append(tuple(input_data))
#
# print(game_protocol)
# print()
#
# place = 1
# for points, winner in enumerate(game_protocol):
#     if place == 3:
#         break
#     for j_points
#     print('{pl} place. {w} ({p})'.format(pl=place, w=winner, p=point))
#     place += 1


# Task 9 Competition protocol
#
# def sort_key(arr):
#     return arr[0]
#
#
# def protocol_competition(count_entries):
#     protocol = list()
#     winners = dict()
#
#     print('Entries (result and name):')
#     while True:
#         if isinstance(count_entries, int) and count_entries >= 3:
#             entry = 1
#             while len(protocol) != count_entries:
#                 player = input(f"{entry} entry: ").split()
#                 if len(player) == 2:
#                     protocol.append((int(player[0]), player[1]))
#                     entry += 1
#                 else:
#                     print('There are must not be any spaces in the name of player.\n')
#             break
#         else:
#             print('Entry must be an integer and more or equal 3. Try again.\n')
#
#     for score, name in sorted(protocol, key=sort_key, reverse=True):
#         if name in winners and score > winners[name]:
#             winners[name] = score
#         elif name not in winners:
#             winners[name] = score
#
#     print()
#
#     if len(winners) < 3:
#         print('There must be at least 3 competitors')
#         protocol_competition(count_entries)
#     else:
#         print('Results of competitions:')
#         place = 1
#         for winner, points in winners.items():
#             print('{0} place. {1} ({2})'.format(place, winner, points))
#             place += 1
#             if place == 4:
#                 break
#
#
# entries_in_protocol = int(input('How much entries in the protocol? '))
# protocol_competition(entries_in_protocol)


# Task 10. My own zip
#
# def generating_my_own_zip(iterable_1, iterable_2):
#     def min_range_len(i1, i2):
#         return min(len(iterable_1), len(iterable_2))
#
#     def dict_keys(dict_1, dict_2, index):
#         key1 = dict_1.keys()
#         key2 = dict_2.keys()
#         return key1, key2
#
#     if isinstance(iterable_1, dict) and isinstance(iterable_2, dict):
#         iter_1, iter_2 = list(enumerate(iterable_1)), list(enumerate(iterable_2))
#         pairs = ((iter_1[key][1], iter_2[key][1]) for key in range(min_range_len(iterable_1, iterable_2)))
#
#     elif isinstance(iterable_1, dict):
#         iter_1 = list(enumerate(iterable_1))
#         pairs = ((iter_1[key][1], iterable_2[key]) for key in range(min_range_len(iterable_1, iterable_2)))
#
#     elif isinstance(iterable_2, dict):
#         iter_2 = list(enumerate(iterable_2))
#         pairs = ((iterable_1[key], iter_2[key][1]) for key in range(min_range_len(iterable_1, iterable_2)))
#
#     else:
#         pairs = ((iterable_1[i_elem], iterable_2[i_elem]) for i_elem in range(min_range_len(iterable_1, iterable_2)))
#
#     return pairs
#
#
# iterable1 = {77: 7, 88: 8, 99: 9}
# iterable2 = (10, 20, 30, 40, 50, 60)
# my_own_zip = generating_my_own_zip(iterable1, iterable2)
# default_zip = zip(iterable1, iterable2)
# print(*my_own_zip)
# print(*default_zip)
