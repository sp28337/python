#
# class CanFly:
#
#     def __init__(self, height, speed):
#         self.__height = height
#         self.__speed = speed
#
#     def __str__(self):
#         return 'Current height: {}\nCurrent speed: {}'.format(self.__height, self.__speed)
#
#     def fly(self):
#         self.__height = 800
#         self.__speed = 180
#
#     def fly_up(self):
#         height = int(input('How high should I fly? '))
#         self.__height = height
#
#     def landing(self):
#         print('successful landing!\n')
#         self.__height = 0
#         self.__speed = 0
#
#     def get_height(self):
#         return self.__height
#
#
# class Robot:
#
#     def __init__(self, model):
#         self.__model = model
#
#     def __str__(self):
#         return 'I am Robot model {}'.format(self.__model)
#
#     def operate(self):
#         pass
#
#
# class Drone(Robot, CanFly):
#
#     def operate(self):
#         print('I\'m conducting reconnaissance from the air')
#
#
# class IronMan(Robot, CanFly):
#
#     def __init__(self, weapon, model):
#         super().__init__(model)
#         self.__weapon = weapon
#
#     def operate(self):
#         print('Protected a military facility from the air using {} weapon'.format(self.__weapon))
#
#
# drone = Drone("R2D2")
# print(drone)
# drone.operate()
# iron_man = IronMan('BLASTER707', "C3PO")
# print(iron_man)
# iron_man.operate()
# iron_man.fly_up()
# print(iron_man)
# iron_man.landing()
# print(iron_man.get_height())
