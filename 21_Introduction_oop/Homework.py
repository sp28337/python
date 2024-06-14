# Task 1. Fight
#
# from random import randint
#
#
# class Unit:
#
#     def __init__(self, name, attack=randint(0, 1), damage=20, health=100, knocks=0):
#         self.name = name
#         self.attack = attack
#         self.damage = damage
#         self.health = health
#         self.knocks = knocks
#
#     def info(self):
#         print('--[Information about winner]--\n'
#               'Name: {}\n'
#               'Health: {}\n'
#               'Damage: {}\n'
#               'Knocks: {}\n'.format(self.name, self.health, self.damage, self.knocks)
#               )
#
#     def got_damage(self):
#         self.health -= 20
#         print('{} got -{} damage!\n'
#               'Current health by {}: {}\n'.format(self.name, self.damage, self.name, self.health))
#
#         if self.health <= 0:
#             print('{} was killed!'.format(self.name))
#             return True
#         return False
#
#     def fight(self):
#         self.attack = randint(0, 1)
#         if self.attack:
#             print('{} is attacking!'.format(self.name))
#             self.knocks += 1
#             return True
#         else:
#             print('{} is waiting for better moment...'.format(self.name))
#             return False
#
#
# warrior1 = Unit('Warrior 1')
# warrior2 = Unit('Warrior 2')
#
# while True:
#     if warrior1.fight():
#         if warrior2.got_damage():
#             warrior1.info()
#             break
#
#     if warrior2.fight():
#         if warrior1.got_damage():
#             warrior2.info()
#             break


# Task 2. Students
#
# from random import randint
# from statistics import mean
#
#
# class Student:
#
#     def __init__(self, name_surname, team, performance=None):
#         self.name_surname = name_surname
#         self.team = team
#         self.performance = [randint(3, 5) for _ in range(5)]
#
#     def info(self):
#         print('Name/Surname: {}\n'
#               'Team number: {}\n'
#               'Performance: {}\n'.format(self.name_surname, self.team, self.performance))
#
#     def student_data(self):
#         data = self.name_surname, self.team, self.performance
#         return data
#
#
# students_list = [] #('Pavel Tarakanov', 1, [4, 5, 3, 3, 3]),
#                    # ('Kristina Tarakanova', 1, [4, 4, 3, 5, 5]),
#                    # ('Egor Tarakanov', 1, [4, 4, 5, 3, 4]),
#                    # ('Nikita Reikch', 2, [4, 4, 3, 5, 4]),
#                    # ('Ivan Pavlov', 3, [3, 4, 3, 4, 4]),
#                    # ('Dima Moiseenko', 2, [5, 3, 3, 5, 5]),
#                    # ('Lesik Dzivinskiy', 3, [3, 4, 3, 3, 5]),
#                    # ('Roma Kuliev', 4, [5, 4, 3, 5, 5]),
#                    # ('Vovan Kokin', 5, [4, 5, 4, 3, 4]),
#                    # ('Sasha Tovarkov', 1, [4, 3, 5, 4, 4])
#
#
# for student in range(10):
#     students_list.append(Student(input('Enter name: '), int(input('Enter team number: '))).student_data())
#     print()
#
# print(*students_list)
# students_list.sort(key=lambda average: mean(average[2]), reverse=True)
#
# print()
#
# for student in students_list:
#     print(student, end='\n')
