# Task 1. Error
#
# import random
#
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         elif isinstance(i_value, dict):
#             i_value[num] = i_key
#         elif isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list[:], 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
#
# change_dict(common_dict)
# print(common_dict)
#
# print(nums_list)
# print(some_dict)
# print(uniq_nums)


# Task 2. Do not understand
# def find_float(string):
#     if '.' in string:
#         for i in ''.join(string.split('.')):
#             if not i.isdigit():
#                 if i == 'e' or i == '-':
#                     continue
#                 result = None
#                 return result
#         else:
#             return True
#     else:
#         for i in string:
#             if not i.isdigit():
#                 if i == 'e' or i == '-':
#                     continue
#                 result = None
#                 return result
#         else:
#             return True
#
#
# def find_list(string):
#     if string.startswith('[') and string.endswith(']'):
#         lst_of_str = string[1:-2].split(', ')
#         if len(lst_of_str) == 1 + string.count(','):
#             return True
#     else:
#         return None
#
#
# def find_tuple(string):
#     if len(string.split()) == 1 + string.count(','):
#         return True
#     else:
#         return None
#
#
# def info_data(some_data):
#
#     if some_data.startswith('{') and ':' in some_data:
#         tip = 'dict (словарь)'
#         m_i = 'mutable (изменяемый)'
#         id_data = id(some_data)
#         return tip, m_i, id_data
#     elif find_list(some_data):
#         tip = 'list (лист)'
#         m_i = 'mutable (изменяемый)'
#         id_data = id(some_data)
#         return tip, m_i, id_data
#     elif some_data.startswith('{') and some_data.count(',') + 1 == len(some_data[1:-1].split()):
#         tip = 'set (множество)'
#         m_i = 'mutable (изменяемый)'
#         id_data = id(some_data)
#         return tip, m_i, id_data
#     elif find_tuple(some_data):
#         tip = 'tuple (кортеж)'
#         m_i = 'immutable (неизменяемый)'
#         id_data = id(some_data)
#         return tip, m_i, id_data
#     elif some_data.isdigit():
#         tip = 'int (целое число)'
#         m_i = 'immutable (неизменяемый)'
#         id_data = id(some_data)
#         return tip, m_i, id_data
#     elif find_float(some_data):
#         tip = 'float (число с плавающей точкой)'
#         m_i = 'immutable (неизменяемый)'
#         id_data = id(some_data)
#         return tip, m_i, id_data
#     else:
#         tip = 'str (строка)'
#         m_i = 'immutable (неизменяемый)'
#         id_data = id(some_data)
#         return tip, m_i, id_data
#
#
# data = input('Enter some data: ')
#
# data_type, mut_immut, id_object = info_data(data)
# print('\nData type: {0}\n{1}\nId: {2}'.format(data_type, mut_immut, id_object))
