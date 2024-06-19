# Task 1. Ships
#
# class Ship:
#     def __init__(self, model):
#         self.model = model
#
#     def __str__(self):
#         return "Model: {}".format(self.model)
#
#     def sail(self):
#         print('Ship {} is sailing somewhere.'.format(self.model))
#
#
# class WarShip(Ship):
#     def __init__(self, model, guns):
#         super().__init__(model)
#         self.guns = guns
#         print('Created warship model: {}'.format(self.model))
#
#     def attack(self):
#         print('warship is attacking with', self.guns)
#
#
# class CargoShip(Ship):
#     def __init__(self, model):
#         super().__init__(model)
#         self.fullness = 0
#         print('Created cargo model: {}'.format(self.model))
#
#     def loading(self):
#         print('It is loading now')
#         self.fullness += 1
#         print('Fullness is: {}\n'.format(self.fullness))
#
#     def unloading(self):
#         print('It is unloading now')
#         self.fullness -= 1
#         print('Fullness is: {}\n'.format(self.fullness))
#
#
# ship1 = CargoShip('AASF442')
# ship2 = WarShip('AS28337', 'Rockets')
# ship2.sail()
# ship2.attack()
# ship1.loading()
# ship1.sail()
#
#
# Task 2. Robots
#
# class Robots:
#     def __init__(self, model):
#         self.model = model
#
#     def operate(self):
#         print('Robot', end=' ')
#
#
# class RobotCleaner(Robots):
#
#     def __init__(self, model):
#         super().__init__(model)
#         self.__fullness = 0
#         print('\n(robot model <{}> initialized)'.format(self.model))
#
#     def __str__(self):
#         return self.model + ' cleaner robot'
#
#     def operate(self):
#         super().operate()
#         self.__fullness += 1
#         print('{} is cleaning floor. Fullness: {}'.format(self.model, self.__fullness))
#
#
# class WarRobot(Robots):
#     def __init__(self, model, weapon):
#         super().__init__(model)
#         self.__weapon = weapon
#         print('\n(robot model <{}> initialized)'.format(self.model))
#
#     def __str__(self):
#         return self.model + ' military robot'
#
#     def operate(self):
#         super().operate()
#         print('{} defended the military object by {}'.format(self.model, self.__weapon))
#
#
# class WarShip(Robots):
#     def __init__(self, model, weapon):
#         super().__init__(WarRobot)
#         self.__deep = 0
#
#
# robot_1 = RobotCleaner('R2D2')
# print(robot_1)
# robot_1.operate()
#
# robot_2 = WarRobot('C3PO', 'ak-47')
# print(robot_2)
# robot_2.operate()
#
# robot_3 = WarRobot('UnderWaterShip333', 'Torpedoes')
# print(robot_3)
# robot_3.operate()
#

# Task 3. Custom exceptions
#
# class DivisionError(Exception):
#     pass
#
#
# with open('numbers.txt', 'r', encoding='utf-8') as file:
#     for row in file:
#         row = row.split()
#         try:
#             if row[0] > row[1]:
#                 raise DivisionError('You cannot divide more by less')
#             else:
#                 print(int(row[0]) / int(row[1]))
#         except DivisionError as e:
#             print(e)
