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
