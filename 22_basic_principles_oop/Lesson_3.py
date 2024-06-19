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


# Task 2. Flight
#
# class CanFly:
#
#     def __init__(self, height=0, speed=0):
#         self.__height = height
#         self.__speed = speed
#
#     def __str__(self):
#         return 'height: {}\nspeed: {}'.format(self.get_height(), self.get_speed())
#
#     def take_off(self):
#         pass
#
#     def flying(self):
#         pass
#
#     def landing(self):
#         print('Landing was successful!')
#         self.set_height(0)
#         self.set_speed(0)
#         print(self.__str__())
#
#     def get_height(self):
#         return self.__height
#
#     def get_speed(self):
#         return self.__speed
#
#     def set_height(self, height):
#         self.__height = height
#
#     def set_speed(self, speed):
#         self.__speed = speed
#
#
# class Butterfly(CanFly):
#
#     def __str__(self):
#         main_info = super().__str__()
#         main_info = '\n'.join((main_info, 'Type: Butterfly\n'))
#         return main_info
#
#     def take_off(self):
#         if not self.get_height():
#             print('Took off!')
#             self.set_height(height=1)
#             print(self.__str__())
#             self.flying()
#         else:
#             print('Already took off.')
#
#     def flying(self):
#         print('Flying !!!')
#         self.set_speed(speed=0.5)
#         print(self.__str__())
#
#     def landing(self):
#         if self.get_height():
#             super().landing()
#         else:
#             print(self.__str__())
#             print('Already on the Earth!\n')
#
#
# class Rocket(CanFly):
#     def __str__(self):
#         main_info = super().__str__()
#         main_info = '\n'.join((main_info, 'Type: Rocket\n'))
#         return main_info
#
#     def take_off(self):
#         print('Rocket took off!')
#         self.set_height(height=500)
#         self.set_speed(speed=1000)
#         print(self.__str__())
#
#     def landing(self):
#         if self.get_speed():
#             self.set_height(height=0)
#             self.boom()
#         else:
#             print('Rocket has not taken off yet!')
#
#     def boom(self):
#         if self.get_speed() and self.get_height() == 0:
#             print('!!!Explosion!!!')
#
#
# # butterfly = Butterfly()
# # butterfly.take_off()
# # butterfly.landing()
# rocket = Rocket()
# rocket.landing()
# rocket.take_off()
# rocket.landing()
