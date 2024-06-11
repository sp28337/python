# Task 1. Vehicle 2
#
# class Toyota:
#     color = 'red'
#     price = 1_000_000
#     max_speed = 200
#     current_speed = 0
#
#     def info(self):
#         print('\nCurrent info:\n'
#               'Color --- {}\n'
#               'Price --- {}\n'
#               'Max speed --- {}\n'
#               'Current speed --- {}'.format(self.color, self.price, self.max_speed, self.current_speed)
#               )
#
#     def set_current_speed(self, speed):
#         self.current_speed = speed
#         print('\nCurrent speed is {}'.format(self.current_speed))
#
#
# car1 = Toyota()
# car1.info()
# car1.set_current_speed(120)
# car1.info()


# Task 2. Family
#
# class Family:
#     surname = 'Common family'
#     money = 100_000
#     having_a_house = False
#
#     def info(self):
#         print('Family info:\n'
#               'Surname --> {}\n'
#               'Money --> {}\n'
#               'House {}\n'.format(self.surname, self.money, self.having_a_house)
#               )
#
#     def earn_money(self, amount):
#         self.money += amount
#         print('[+] {}$\n'
#               'Current balance: {}\n'.format(amount, self.money)
#               )
#
#     def buy_house(self, price, discount=0):
#         price -= price * discount / 100
#         print('Try to by a house')
#         if self.money >= price:
#             self.money -= price
#             self.having_a_house = True
#             print('House successfully purchased!\n'
#                   'Current balance: {}\n'.format(self.money))
#         else:
#             print('Purchased unsuccessfully, you have not enough money!\n')
#
#
# my_family = Family()
# my_family.info()
# my_family.buy_house(1_000_000, 90)
# my_family.info()
