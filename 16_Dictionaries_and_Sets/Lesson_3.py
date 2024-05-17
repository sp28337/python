# Task 1. Family member
#
# def find_name(lists, name):
#     for j in range(len(lists.get('children'))):
#         if lists.get('children')[j].get('name') == name:
#             return True
#     else:
#         return 'Noname'
#
#
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
#
# for i in family_member.keys():
#     if i == 'hobbies':
#         print(i, ':', ', '.join(family_member[i]), end='')
#         print()
#     elif i == 'children':
#         child = [family_member[i][x]['name'] for x in range(len(family_member[i]))]
#         print(i, ':', ', '.join(child))
#     else:
#         print(i, ':', family_member[i])
#
# print()
#
# name_to_find = input('What name need to find? ')
# question = find_name(family_member, name_to_find)
# print(question)
