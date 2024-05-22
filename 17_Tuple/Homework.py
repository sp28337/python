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

