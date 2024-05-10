# def horrible_cod(main, first, second):
#     main.extend(first)
#     print(f"Count of 5 digits at first unification {main.count(5)}")
#     for i in main:
#         if i == 5:
#             main.remove(i)
#     main.extend(second)
#     print(f"Count of 3 digits at first unification {main.count(3)}")
#     print(f"Final list: {main}")
#
#
# main_list = [1, 5, 3]
# first_list = [1, 5, 1, 5]
# second_list = [1, 3, 1, 5, 3, 3]
#
# horrible_cod(main_list, first_list, second_list)


# class_1 = list(range(160, 177, 2))
# class_2 = list(range(162, 181, 3))
# two_classes = class_2 + class_1
# two_classes.sort()
# print(two_classes)


# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],
#         ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
# count = total_cost = 0
# thing = input('Name of a detail: ')
# for i in shop:
#     if i[0] == thing:
#         count += 1
#         total_cost += i[1]
# print(f"Count of details - {count}\nTotal cost: {total_cost}")


# def dress_code(answer, guests):
#     name = input('Guest name: ')
#     if len(guests) <= 6:
#         if answer == 'came':
#             print(f"Hello, {name}!")
#             guests.append(name)
#         elif answer == 'gone':
#             print(f"Goodbye, {name}!")
#             guests.remove(name)
#     else:
#         print(f"Sorry, {name}, there are not free space for you.")
#     print(f"\nBy the moment there are {len(guests)} people: {guests}")
#
#
# guests_list = ['Petya', 'Ivan', 'Sasha', 'Liza', 'Katty']
# print(f"By the moment there are {len(guests_list)} people: {guests_list}")
#
# answer_x = input('Has the guest came or gone?: ')
# while answer_x != 'time to bed':
#     dress_code(answer_x, guests_list)
#     answer_x = input('Has the guest came or gone?: ')
# else:
#     print('\nParty was finished. Everyone went to bed.')


# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]
#
# time_sound = 0
#
# songs = int(input('Enter count of songs: '))
# for j in range(songs):
#     print(f"Name of {j + 1} song:", end=' ')
#     song_name = input('Enter name of a song: ')
#     for i in violator_songs:
#         if i[0] == song_name:
#             time_sound += i[1]
#             break
# print(f"Total time: {round(time_sound, 2)} minutes")


# def make_list(length):
#     new_list = []
#     for _ in range(length):
#         new_list.append(int(input('Enter number: ')))
#     return new_list
#
#
# list_1 = make_list(int(input('Enter length of first list: ')))      #[1, 2, 3]
# list_2 = make_list(int(input('Enter length of second list: ')))     #[2, 4, 6, 3, 3, 2, 1]
#
# print(list_1)
# print(list_2)
#
# list_1.extend(list_2)
# print(list_1)
# for i in list_1:
#     for _ in range(list_1.count(i) - 1):
#         list_1.remove(i)
#
# print('New first list with uniques elements:', list_1)


# def make_list_skates(number_of_skates):
#     new_list = []
#     for i in range(number_of_skates):
#         print(f"Size of {i + 1} pair:", end=' ')
#         size = int(input())
#         new_list.append(size)
#     return new_list
#
#
# def make_list_people(number_of_people):
#     new_list = []
#     for i in range(number_of_people):
#         print(f"Size of leg {i + 1} people:", end=' ')
#         size = int(input())
#         new_list.append(size)
#     return new_list
#
#
# number_skates = int(input('Enter number of skates: '))
# skates = make_list_skates(number_skates)#[41, 40, 39, 42]
# number_people = int(input('Enter number of people: '))
# people = make_list_people(number_people)#[42, 41, 42]
# count = 0
# skates.sort()
# people.sort()
# for men in people:
#     for size in skates:
#         if men <= size:
#             skates.remove(size)
#             count += 1
#             break
#
# print(count)


# people = int(input('Enter the number of people: '))
# move_index = int(input('Enter the number K: '))
# list_people = list(range(1, people + 1))
# start_index = 0
# while len(list_people) >= 2:
#     print(f"\nCurrent round of people: {list_people}")
#     if start_index >= len(list_people):
#         start_index = 0
#         print(f"Start counting from number: {list_people[start_index]}")
#     else:
#         print(f"Start counting from number: {list_people[start_index]}")
#     if len(list_people) * 2 <= move_index:
#         leaving_people_index = abs(len(list_people) * (move_index // len(list_people)) - move_index) - 1 + start_index
#         print(f"People number {list_people[leaving_people_index]} going away.")
#         start_index = leaving_people_index
#
#     elif len(list_people) < move_index:
#         leaving_people_index = abs(len(list_people) - move_index) - 1 + start_index
#         print(f"People number {list_people[leaving_people_index]} going away.")
#         start_index = leaving_people_index
#     else:
#         leaving_people_index = start_index + move_index - 1
#         if leaving_people_index >= len(list_people):
#             leaving_people_index = abs(leaving_people_index - len(list_people))
#         print(f"People number {list_people[leaving_people_index]} going away.")
#         start_index = leaving_people_index
#     list_people.remove(list_people[leaving_people_index])
# print(f"Last people is: {list_people[0]}")


# friends = int(input('Count of friends: '))
# debts = int(input('Count of debts: '))
#
# friends_list = []
# for _ in range(friends):
#     friends_list.append(0)
#
# for i in range(debts):
#     print(f"\nDebt {i + 1}")
#     to_index = int(input('For whom?: '))
#     from_index = int(input('From who?: '))
#     if to_index == from_index:
#         print('Error, cannot borrow from yourself.')
#     else:
#         size = int(input('How much?: '))
#         if size >= 0:
#             friends_list[to_index - 1] += size
#             friends_list[from_index - 1] -= size
#         else:
#             friends_list[to_index - 1] -= size
#             friends_list[from_index - 1] += size
#
# print(f"\nBalance of friends:")
# for i in range(friends):
#     print(f"{i + 1}: {friends_list[i]}")


# seq = []
# count_numbers = int(input('Enter count of numbers: '))
# for _ in range(count_numbers):
#     number = int(input('Enter the number: '))
#     seq.append(number)
#
# print("Sequence:", end=' ')
# for i in seq:
#     print(i, end=' ')
# print()
#
# rev_seq = seq[::-1]
# while rev_seq[0] == seq[-1]:
#     rev_seq.remove(rev_seq[0])
#
# print(f"Need to add digits: {len(rev_seq)}\nNumbers:", end=' ')
# for j in rev_seq:
#     print(j, end=' ')
# print()