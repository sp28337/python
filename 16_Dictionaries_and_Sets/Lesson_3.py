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


# Task 2. Players
#
# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# resting_A_players = list()
# workout_B_players = list()
# traveling_C_players = list()
#
# for player in players_dict.values():
#     if player.get('team') == 'A' and player.get('status') == 'Rest':
#         resting_A_players.append(player.get('name'))
#     elif player.get('team') == 'B' and player.get('status') == 'Training':
#         workout_B_players.append(player.get('name'))
#     elif player.get('team') == 'C' and player.get('status') == 'Travel':
#         traveling_C_players.append(player.get('name'))
#
# print("Team A resting members: {0}\nTeam B training members: {1}\nTeam C traveling members: {2}"
#       .format(', '.join(resting_A_players), ', '.join(workout_B_players), ', '.join(traveling_C_players)))
