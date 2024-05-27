# Task 1. Work with file
#
# def what_to_do(question,
#                error='Wrong input. Please enter <yes> or <no>.',
#                retries=5):
#     while True:
#         answer = input(question).lower()
#         if answer == 'yes':
#             return 1
#         elif answer == 'no':
#             return 0
#         retries -= 1
#         if retries == 0:
#             break
#         print(error)
#         print('Last retries:', retries)
#
#
# what_to_do('Do you really wanna go out?')
# what_to_do('Do you wanna delete file?', 'So delete or not?')
# what_to_do('Write a file?', retries=2)


# Task 2. Accumulation of values
#
# def add_num(num, lst=None):
#     lst = list()
#     lst.append(num)
#     print(lst)
#
# add_num(5)
# add_num(10)
# add_num(15)


# Task 3. Help to friend
#
# # def create_dict(input_data):
# #     template = dict()
# #     if isinstance(input_data, dict):
# #         return input_data
# #     elif isinstance(input_data, int) or isinstance(input_data, float) or isinstance(input_data, str):
# #         template.setdefault(input_data, input_data)
# #         return template
# #     else:
# #         return input_data
# #
# #
# # def data_preparation(lst):
# #     lst_copy = []
# #     for i_element in lst:
# #         lst_copy.append(create_dict(i_element))
# #         if i_element == create_dict(i_element) and not isinstance(i_element, dict):
# #             lst_copy.remove(i_element)
# #     return lst_copy
#
#
# def data_preparation(s_data):
#     lst_copy = []
#     for i in s_data:
#         if isinstance(i, dict):
#             lst_copy.append(i)
#         elif isinstance(i, int) or isinstance(i, float) or isinstance(i, str):
#             new_dict = dict()
#             new_dict.setdefault(i, i)
#             lst_copy.append(new_dict)
#     return lst_copy
#
#
# data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)
#


