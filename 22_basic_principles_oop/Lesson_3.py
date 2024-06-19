# Task 1. Units
#
# class Unit:
#     __count = 1
#
#     def __init__(self, health):
#         self.__health = health
#         print('(unit {} initialized)'.format(self.__count))
#         self.set_count()
#
#     def get_health(self):
#         return self.__health
#
#     def set_count(self):
#         Unit.__count += 1
#
#     def set_health(self, health):
#         self.__health = health
#
#     def get_damage(self, damage):
#         pass
#
#
# class Soldier(Unit):
#
#     def get_damage(self, damage):
#         new_health = self.get_health() - damage
#         self.set_health(new_health)
#
#
# class Citizen(Unit):
#     def get_damage(self, damage):
#         new_health = self.get_health() - 2 * damage
#         self.set_health(new_health)
#
#
# soldier = Soldier(100)
# citizen = Citizen(100)
# soldier.get_damage(10)
# citizen.get_damage(20)
# print(soldier.get_health())
# print(citizen.get_health())
