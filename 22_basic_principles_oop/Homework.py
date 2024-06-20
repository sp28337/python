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
