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
# class Water:
#     def __str__(self):
#         return 'Water'
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Vapor()
#         elif isinstance(other, Earth):
#             return Dirt()
#         else:
#             return None
#
#
# class Air:
#     def __str__(self):
#         return 'Air'
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Dust()
#         else:
#             return None
#
#
# class Fire:
#     def __str__(self):
#         return 'Fire'
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Lightning()
#         elif isinstance(other, Water):
#             return Vapor()
#         elif isinstance(other, Earth):
#             return Lava()
#         else:
#             return None
#
#
# class Earth:
#     def __str__(self):
#         return 'Earth'
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lava()
#         elif isinstance(other, Water):
#             return Dirt()
#         else:
#             return None
#
#
# class Storm:
#     def __str__(self):
#         return 'Storm'
#
#
# class Vapor:
#     def __str__(self):
#         return 'Vapor'
#
#
# class Dirt:
#     def __str__(self):
#         return 'Dirt'
#
#
# class Lightning:
#     def __str__(self):
#         return 'Lightning'
#
#
# class Dust:
#     def __str__(self):
#         return 'Dust'
#
#
# class Lava:
#     def __str__(self):
#         return 'Lava'
#
#
# water = Water()
# air = Air()
# fire = Fire()
# earth = Earth()
#
# print(air + water)
# print(earth + water)
# print(fire + water)
# print(water + fire)
# print(fire + earth)
# print(fire + air)


# Task 7. Cohabitation
#
# from random import randint
#
#
# class Person:
#
#     def __init__(self, name, home, satiety=50):
#         self.name = name
#         if isinstance(home, House):
#             self.home = home
#         else:
#             raise ValueError('<home> must be class object House.')
#         self.satiety = satiety
#         print('{} INITIALIZED'.format(self.name))
#
#     def info(self):
#         print('INFO {}\nSatiety: {}'.format(self.name, self.satiety))
#
#     def __str__(self):
#         return '{} INITIALIZED'.format(self.name)
#
#     def eat(self):
#         if self.home.food >= 10:
#             print('{} is eating...'.format(self.name))
#             self.satiety += 10
#             self.home.food -= 10
#
#         else:
#             self.satiety += self.home.food
#             self.home.food = 0
#
#     def work(self):
#         self.satiety -= 10
#         self.home.money += 10
#
#     def play(self):
#         print('{} is playing.'.format(self.name))
#         self.satiety -= 10
#
#     def go_store(self):
#         if self.home.money >= 10:
#             self.home.food += 10
#             self.home.money -= 10
#
#     def live(self):
#         rand_cub_num = randint(1, 6)
#         if self.satiety < 0:
#             print('{} died due to hunger!'.format(self.name))
#             return False
#         if self.satiety < 20 and self.home.food >= 10:
#             self.eat()
#
#         elif self.home.food < 10 and self.home.money > 0:
#             self.go_store()
#             print('{} go shop.'.format(self.name))
#
#         elif self.home.money < 50:
#             self.work()
#
#         elif rand_cub_num == 1:
#             self.work()
#
#         elif rand_cub_num == 2:
#             self.eat()
#
#         else:
#             self.play()
#         return True
#
#
# class House:
#
#     def __init__(self, food=50, money=0):
#         self.food = food
#         self.money = money
#
#
# def simulate_life(days):
#     home1 = House()
#     alex = Person('Alex', home1)
#     ivan = Person('Ivan', home1)
#
#     for day in range(1, days + 1):
#         print('Day', day)
#         alex_alive = alex.live()
#         ivan_alive = ivan.live()
#
#         if not alex_alive or not ivan_alive:
#             print('Experiment finished earlier!')
#             break
#
#         print(f'{alex.name}:\nsatiety - {alex.satiety}\nmoney - {alex.home.money}')
#         print(f'{ivan.name}:\nsatiety - {ivan.satiety}\nmoney - {ivan.home.money}')
#
#     else:
#         print('Both people lived 365 days!')
#
#
# simulate_life(365)
#

# from random import randint
#
#
# class Person:
#
#     def __init__(self, name, house, satiety=50, alive=True):
#         self.name = name
#         self.alive = alive
#         if isinstance(house, House):
#             self.house = house
#         else:
#             raise ValueError("<house> must be object of <House> class")
#         self.satiety = satiety
#         print('-(Person {} initialized)-'.format(self.name))
#
#     def status(self):
#         print('<{0}> INFO\n'
#               'Name: {0}\n'
#               'Satiety: {1}\n'
#               'Money in house: {2}\n'
#               'Food in house: {3}\n'.format(self.name, self.satiety, self.house.money, self.house.food)
#               )
#
#     def eat(self):
#         if self.house.food > 0:
#             print('{} is eating...'.format(self.name))
#             self.satiety += randint(1, 6)
#             print('[+] Satiety up!')
#             self.house.food -= randint(1, 6)
#             print('[-] Food runs out!\n')
#         else:
#             print('(Frighten is empty) {} is starving\n'.format(self.name))
#             self.go_store()
#         self.status()
#
#     def work(self):
#         if self.satiety > 5:
#             print('{} is working...'.format(self.name))
#             self.satiety -= randint(1, 6)
#             print('[-] Satiety runs out!')
#             self.house.money += 5
#             print('[+] Earned!\n')
#         else:
#             self.eat()
#         self.status()
#
#     def play(self):
#         print('{} is playing...'.format(self.name))
#         self.satiety -= randint(1, 6)
#         print('[-] Satiety runs out!\n')
#         # self.status()
#
#     def go_store(self):
#         if self.house.money > 0:
#             print('{} went to store...'.format(self.name))
#             self.house.money -= randint(1, 6)
#             print('[-] Money runs out!')
#             self.house.food += randint(1, 6)
#             print('[+] Food up!\n')
#         else:
#             self.satiety -= randint(1, 6)
#             print('[-] Satiety runs out!\n')
#             print('(Wallet is empty...) {} may not get purchases!'.format(self.name))
#         self.status()
#
#
# class House:
#
#     def __init__(self, number, food=50, money=0):
#         self.number = number
#         self.food = food
#         self.money = money
#         print('--(House {} initialized)--'.format(self.number))
#
#     def info(self):
#         print('HOUSE\n'
#               'Fridge: {} food\n'
#               'Wallet: {}$\n'.format(self.food, self.money)
#               )
#
#
# def logic_people(person):
#     if person.satiety >= 0:
#         random_number = randint(1, 6)
#         if person.satiety < 20:
#             person.eat()
#         elif person.house.food < 10:
#             person.go_store()
#         elif person.house.money < 50:
#             person.work()
#         elif random_number == 1:
#             person.work()
#         elif random_number == 2:
#             person.eat()
#         else:
#             person.play()
#     else:
#         print('\n\n{} DIED!!!\n\n'.format(person.name))
#         person.alive = False
#
#
# leskin_house = House(2, 50)
# leskin_house.info()
#
# lesik = Person('Lesik', leskin_house, 20)
# lesik.status()
#
# alena = Person('Alena', leskin_house)
# alena.status()
#
# days = 0
#
# while True:
#     if days > 365:
#         print('!!! Experimental subjects are alive after {} days experiment !!!'.format(days))
#         break
#     print('Day number - {}'.format(days))
#     if lesik.alive or alena.alive:
#         if lesik.alive:
#             logic_people(lesik)
#         if alena.alive:
#             logic_people(alena)
#     else:
#         break
#     days += 1


# Task 8. Black-Jack
#
# import random
#
#
# class CardDeck:
#
#     def __init__(self):
#         self.card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', True] * 4
#         random.shuffle(self.card_deck)
#
#     def take_card(self):
#         return self.card_deck.pop()
#
#     def shuffle_cards(self):
#         random.shuffle(self.card_deck)
#
#
# def main_menu():
#     print('***[COMMANDS]***\n'
#           '<START> --- play Black-Jack\n'
#           '<OUT> --- exit app\nEnter a command:', end=' '
#           )
#     command = input().lower()
#     if command in ('start', 's'):
#         start_game()
#
#
# def start_game():
#     my_cards, ai_cards = [], []
#     points = 0
#     card_deck = CardDeck()
#
#     print('\nWelcome back to Black-JacK!')
#     print('...dealing cards...\n')
#
#     for _ in range(2):
#         my_cards.append(card_deck.take_card())
#         ai_cards.append(card_deck.take_card())
#     print('Your cards: {}'.format(my_cards))
#     points = check_my_points(my_cards)
#     print('Your points: {}\n'.format(points))
#     while True:
#         if points > 20:
#             print('Yor points is: {}'.format(points))
#             ai_score = ai_points(ai_cards)
#             print('AI points is: {}'.format(ai_score))
#             if ai_score > points:
#                 print('---YOU LOOSE---\n')
#             elif ai_score < points:
#                 print('!!!---YOU WIN---!!!\n')
#             else:
#                 print('???--DRAW---???\n')
#             main_menu()
#         else:
#             user_move = input('Take another card? ')
#             if user_move in ('y', 'yes'):
#                 my_cards.append(card_deck.take_card())
#                 points = check_my_points(my_cards)
#                 print('My score: {}'.format(points))
#             else:
#                 print('\n***[RESULTS]***\n')
#                 print('Yor points is: {}'.format(points))
#                 ai_score = ai_points(ai_cards)
#                 print('AI points is: {}'.format(ai_score))
#                 if ai_score > points:
#                     print('---YOU LOOSE---\n')
#                 elif ai_score < points:
#                     print('!!!---YOU WIN---!!!\n')
#                 else:
#                     print('???--DRAW---???\n')
#                 main_menu()
#
#
# def check_my_points(lst):
#     score = 0
#     for card in lst:
#         if isinstance(card, int):
#             score += card
#         elif isinstance(card, str):
#             score += 10
#         elif isinstance(card, bool):
#             if score <= 10:
#                 score += 11
#             else:
#                 score += 1
#     return score
#
#
# def ai_points(lst):
#     score = 0
#     for card in lst:
#         if isinstance(card, int):
#             score += card
#         elif isinstance(card, str):
#             score += 10
#         elif isinstance(card, bool):
#             if score <= 10:
#                 score += 11
#             else:
#                 score += 1
#     return score
#
#
# def results(sc, ai):
#     print('You got {} points\nAI got {} points'.format(sc, ai))
#
#
# main_menu()


# Task 9. XO
#
#
# board_places = list(range(1, 10))
#
#
# def draw_board(board):
#     print('-' * 13)
#     for row in range(3):
#         print('| {0} | {1} | {2} |'.format(board[row * 3 + 0], board[row * 3 + 1], board[row * 3 + 2]))
#         print('-' * 13)
#
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input('Where to put {}? '.format(player_token))
#         try:
#             player_answer = int(player_answer)
#         except ValueError:
#             print('Incorrect type! Are you sure that entered an int?')
#             continue
#         if 1 <= player_answer <= 9:
#             if str(board_places[player_answer - 1]) not in 'XO':
#                 board_places[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print('This place is beasy!')
#         else:
#             print('Incorrect number of place! Must be from 1 to 9.')
#
#
# def check_win(board):
#     win_places = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_places:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board_places)
#         if counter % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         counter += 1
#
#         tmp = check_win(board_places)
#         if tmp:
#             print(tmp, 'win!')
#             win = True
#             break
#         elif tmp == 9:
#             print('Draw!')
#             break
#     draw_board(board_places)
#
#
# main(board_places)
# input("Press Enter to out!")
