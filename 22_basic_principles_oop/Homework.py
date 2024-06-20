# Task 1. Taxes
#
# class Property:
#     """
#     Basic class for property
#
#     __tax_lst: list of taxes
#
#     Args:
#         worth (int): estimate of item
#     """
#
#     __tax_lst = []
#
#     def __init__(self, worth):
#         self.__worth = worth
#
#     def get_worth(self):
#         """
#         Getter for worth
#
#         :return: __worth
#         :rtype: int
#         """
#         return self.__worth
#
#     def get_tax_lst(self):
#         return self.__tax_lst
#
#     def set_tax_lst(self, item):
#         """
#         Setter for appending tax value into __tax_lst
#         :param item: tax
#         :type item: float
#         """
#         self.__tax_lst.append(item)
#         print('({} was added into property list)'.format(item))
#
#     def tax(self):
#         pass
#
#
# class Apartment(Property):
#     """
#     Class Apartment. Parent: Property
#
#     Args:
#         worth (int): estimate of item
#     """
#
#     def __init__(self, worth):
#         super().__init__(worth)
#         self.set_tax_lst(self.tax())
#
#     def tax(self):
#         """
#         Calculate a tax value
#         :return: apartment_tax
#         :rtype: float
#         """
#         apartment_tax = round(self.get_worth() / 1000, 2)
#         return apartment_tax
#
#
# class Car(Property):
#     """
#     Class Car. Parent: Property
#
#     Args:
#         worth (int): estimate of item
#     """
#
#     def __init__(self, worth):
#         super().__init__(worth)
#         self.set_tax_lst(self.tax())
#
#     def tax(self):
#         """
#          Calculate a tax value
#          :return: apartment_tax
#          :rtype: float
#          """
#         car_tax = round(self.get_worth() / 200, 2)
#         return car_tax
#
#
# class CountryHouse(Property):
#     """
#     Class CountryHouse. Parent: Property
#
#     Args:
#         worth (int): estimate of item
#     """
#
#     def __init__(self, worth):
#         super().__init__(worth)
#         self.set_tax_lst(self.tax())
#
#     def tax(self):
#         """
#          Calculate a tax value
#          :return: apartment_tax
#          :rtype: float
#          """
#         country_house = round(self.get_worth() / 500, 2)
#         return country_house
#
#
# def main():
#     """Main thread"""
#
#     property_lst = ['apartment', 'car', 'country house']
#     money = int(input('How much money do you have? '))
#     for index, item in enumerate(property_lst):
#         cost = int(input('Enter estimate of {} '.format(item)))
#         if item.lower() == 'apartment':
#             floor = Apartment(cost)
#         elif item.lower() == 'car':
#             car = Car(cost)
#         elif item.lower() == 'country house':
#             country_house = CountryHouse(cost)
#     else:
#         zip_result = zip(property_lst, Property(0).get_tax_lst())
#         print()
#         for index, line in enumerate([*zip_result]):
#             print('Tax for {} is {}'.format(line[0], line[1]))
#             if line[1] > money:
#                 print('You are missing {}$ for paying tax!'.format(money - line[1]))
#                 money -= line[1]
#
#
# main()


# Task 2. Karma
#
# from random import randint
#
#
# class KillError(Exception):
#
#     def __str__(self):
#         return 'KillError'
#
#
# class DrunkError(Exception):
#     def __str__(self):
#         return 'DrunkError'
#
#
# class CarCrashError(Exception):
#     def __str__(self):
#         return 'CarCrashError'
#
#
# class GluttonyError(Exception):
#     def __str__(self):
#         return 'GluttonyError'
#
#
# class DepressionError(Exception):
#     def __str__(self):
#         return 'DepressionError'
#
#
# class Life:
#     """
#     class Life for simulating life
#
#     __carma: points of karma
#
#     Args:
#         days (int): count of days
#     Attributes:
#           my_exceptions (tuple): tuple of custom exceptions
#     """
#
#     __karma = 0
#     my_exceptions = (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError)
#
#     def __init__(self, days=0):
#         print('(New life was initialized)')
#         self.__days = 0
#
#     def set_karma(self, val):
#         """
#         Setter for karma
#
#         :param val: value to increase karma
#         :type val: int
#         """
#         self.__karma += val
#         print('Carma has increased on {} points'.format(val))
#
#     def set_days(self):
#         """
#         Setter for days. Increase days count +1 each time it is invoked.
#         """
#         self.__days += 1
#         print('Day number {}'.format(self.__days))
#
#     def get_karma(self):
#         """
#         Getter for karma
#
#         :return: __karma
#         :rtype: int
#         """
#         return self.__karma
#
#     def get_days(self):
#         """
#         Getter for days
#
#         :return: __days
#         :rtype: int
#         """
#         return self.__days
#
#     def one_day(self):
#         """
#         Day simulation. Calls set_days to increase days count.
#
#         Args:
#             random_number (int): probability 1 in 10
#             random_index (int): random error
#
#         :return: set_karma
#         :raise Exception: if random_number = 1
#         """
#
#         self.set_days()
#         print('Day {}'.format(self.__days))
#         random_number = randint(1, 10)
#         random_index = randint(0, 4)
#         if random_number == 1:
#             raise self.my_exceptions[random_index](self.my_exceptions[random_index])
#         else:
#             return self.set_karma(randint(1, 7))
#
#
# def write_exception_to_log(string):
#     """
#     Write data to file.
#
#     :param string: name of error
#     :type string: str
#     """
#
#     with open('karma.log', 'a', encoding='utf-8') as file:
#         file.write(string + '\n')
#     print('{} was successfully written into karma.log\n'.format(string))
#
#
# life_simulate = Life()
# while life_simulate.get_karma() < 500:
#     try:
#         life_simulate.one_day()
#     except Exception as e:
#         print(e)
#         write_exception_to_log(e.__str__())
# else:
#     print('Your carma got 500 points')
