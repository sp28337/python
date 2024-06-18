# Task 1. Ships
#
# class Ship:
#     def __init__(self, model):
#         self.model = model
#
#     def __str__(self):
#         return "{}".format(self.model)
#
#     def info(self):
#         print('Ship model is {}'.format(self.model))
#
#     def sail(self):
#         print('Ship {} is sailing somewhere.'.format(self.model))
#
#
# class WarShip(Ship):
#     def __init__(self, model, guns):
#         super().__init__(self)
#         self.guns = guns
#         self.model = model
#         print('Created warship model: {}'.format(self.model))
#
#     def attack(self):
#         print('warship is attacking with', self.guns)
#
#
# class CargoShip(Ship):
#     def __init__(self, model):
#         super().__init__(self)
#         self.fullness = 0
#         self.model = model
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
