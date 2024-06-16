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


# Task 3. Circle
#
# import math
#
#
# class Circle:
#     def __init__(self, x=0, y=0, radius=1):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def info(self):
#         print('--INFO--\nCenter of the circle: ({}, {})\nRadius: {}\n'.format(self.x, self.y, self.radius))
#
#     def find_area(self):
#         area = math.pi * math.pow(self.radius, 2)
#         print(area)
#         return area
#
#     def find_perimeter(self):
#         c = 2 * math.pi * self.radius
#         return c
#
#     def increase_in(self, times):
#         self.radius *= times
#
#     def is_intersection(self, other):
#         distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
#         return distance < self.radius + other.radius
#
#
# circle1 = Circle(0, 0, 1)
# circle1.info()
#
# circle2 = Circle(1, 5, 5)
# circle2.info()
#
#
# if circle2.is_intersection(circle1):
#     print('Intersection')
# else:
#     print('Not intersection')


# Task 4. Fathers, mothers, children
#
# from random import randint
#
#
# class Parent:
#     child_lst = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Parent {0} initialized)'.format(self.name))
#
#     def info(self):
#         print('[Current info about {}]'.format(self.name))
#         print('Name: {}\n'
#               'Age: {}\n'
#               'Children list: {}\n'.format(self.name, self.age, self.child_lst)
#               )
#
#     def calm_child(self, other):
#         if other.mood < 3:
#             print('{} trying to calm the {} down'.format(self.name, other.name))
#             print('(in process...)')
#             if randint(0, 1):
#                 print('{} successfully calmed the child!'.format(self.name))
#                 print('{} feel much better! Mood changed <{}> --> <{}>\n'.format(other.name,
#                                                                                  other.mood_dict[other.mood],
#                                                                                  other.mood_dict[other.mood + 1]))
#                 other.mood += 1
#             else:
#                 print('{} could not calm the child down!\n'.format(self.name))
#         else:
#             print('The child is already in a good mood.\n')
#
#     def feed_child(self, other):
#         if other.hungry:
#             other.hungry = False
#             other.mood = 3
#
#             print('Parent {} fed the {}\n'.format(self.name, other.name))
#         else:
#             print('{} does not hungry!'.format(other.name))
#
#
# class Child:
#     mood_dict = {0: 'awful', 1: 'bad', 2: 'satisfied', 3: 'glad', 4: 'happy'}
#
#     def __init__(self, name, age, mood=2, hungry=0):
#         self.name = name
#         self.age = age
#         self.mood = mood
#         if self.mood in (0, 1):
#             self.hungry = bool(1)
#         else:
#             self.hungry = bool(0)
#         Parent.child_lst.append(self.data())
#         print('(Child {0} initialized)'.format(self.name))
#
#     def data(self):
#         data = (self.name, self.age)
#         return data
#
#     def info(self):
#         print('[Current info about {}]'.format(self.name))
#         print('Name: {}\n'
#               'Age: {}\n'
#               'Mood: {}\n'
#               'Hungry: {}\n'.format(self.name, self.age, Child.mood_dict[self.mood], self.hungry)
#               )
#
#
# child1 = Child('Alisa', 4, 2)
# child1.info()
# child2 = Child('Alik', 14, 1)
# child2.info()
#
# print()
#
# parent1 = Parent('Ivan', 30)
# parent1.info()
# parent2 = Parent('Nikita', 31)
# parent2.info()
#
# print()
#
# parent2.calm_child(child2)
# child2.info()


# Task 5. Happy farm 2
#
# crop = []
#
#
# class Gardener:
#     def __init__(self, name, garden):
#         self.name = name
#         self.garden = garden
#         print('New gardener hired!')
#
#     def info(self):
#         print('Name: {}\nGarden: {}\n'.format(self.name, self.garden.name))
#
#     def care_garden(self):
#         if not all([i_potato.is_ripe() for i_potato in self.garden.potatoes]):
#             print('Gardener {} taking care of the {}'.format(self.name, self.garden.name))
#             print('(in process...)')
#             self.garden.grow_all()
#             print()
#         else:
#             print('Planting new potatoes...\n')
#             self.garden.potatoes = [Potato(index) for index in range(1, self.garden.count + 1)]
#
#     def harvest(self):
#         if all([i_potato.is_ripe() for i_potato in self.garden.potatoes]):
#             result = 5 * self.garden.count
#             self.garden.count = 0
#             self.garden.potatoes = [Potato(0) for index in range(0)]
#             print(self.garden.potatoes)
#             print('Your yield is: {}\nNow you can plant new potatoes!\n'.format(result))
#             return result
#         else:
#             print('Potato does not ripe yet! You should take care about your garden!\n')
#
#
# class Potato:
#     states = {0: 'seedling', 1: 'crossbreed', 2: 'flowering', 3: 'ripe'}
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 3:
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):
#         print('Potato {} now {}'.format(self.index, Potato.states[self.state]))
#
#
# class PotatoGarden:
#
#     def __init__(self, count=0):
#         self.count = count
#         self.name = 'Potato_garden'
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print('Potato growing up!')
#         for i_potato in self.potatoes:
#             i_potato.grow()
#
#     def are_all_ripe(self):
#         if PotatoGarden().potatoes:
#             if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
#                 print('Potato does not ripe yet!\n')
#             else:
#                 print('All potatoes is ripe!\n')
#         else:
#             print('Garden is not planted!\n')
#
#
# my_garden = PotatoGarden(5)
# my_garden.are_all_ripe()
# for _ in range(1):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()
#
# gardener = Gardener('Oleg', my_garden)
# gardener.info()
# gardener.care_garden()
# gardener.harvest()
# gardener.care_garden()
# crop.append(gardener.harvest())
#
# my_garden.are_all_ripe()
# gardener.care_garden()
# gardener.care_garden()
# my_garden = PotatoGarden(10)
# gardener.care_garden()


# Task 6. Magic
#
# class Magic:
#
#     help = ('     ВИДЫ МАГИИ',
#             'Вода + Воздух = Шторм',
#             'Вода + Огонь = Пар',
#             'Вода + Земля = Грязь',
#             'Воздух + Огонь = Молния',
#             'Воздух + Земля = Пыль',
#             'Огонь + Земля = Лава\n')
#
#     def __init__(self, name):
#         self.name = name
#         print('[+] ({} initialized)'.format(self.name))
#
#     def __add__(self, other):
#         if isinstance(other, Magic):
#             if self.name == 'Water':
#                 if other.name == 'Air':
#                     return Magic('Storm')
#                 elif other.name == 'Fire':
#                     return Magic('Steam')
#                 elif other.name == 'Ground':
#                     return Magic('ground')
#             elif self.name == 'Air':
#                 if other.name == 'Fire':
#                     return Magic('Lightning')
#                 elif other.name == 'Ground':
#                     return Magic('Dust')
#                 elif other.name == 'Water':
#                     return Magic('Storm')
#             elif self.name == 'Fire':
#                 if other.name == 'Ground':
#                     return Magic('Lava')
#                 if other.name == 'Air':
#                     return Magic('Lightning')
#                 elif other.name == 'Water':
#                     return Magic('Steam')
#
#             elif self.name == 'Ground':
#                 if other.name == 'Fire':
#                     return Magic('Lava')
#                 elif other.name == 'Air':
#                     return Magic('Dust')
#                 elif other.name == 'Water':
#                     return Magic('Dirt')
#         else:
#             raise ValueError('Right operand must be Magi')
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#     def info(self):
#         print('\n---INFO---\nName: {}\n'.format(self.name))
#
#
# water = Magic('Water')
# air = Magic('Air')
# fire = Magic('Fire')
# ground = Magic('Ground')
#
# print()
#
# storm = air + water
# storm.info()
# print('\n'.join(Magic.help))
# lava = fire + ground
