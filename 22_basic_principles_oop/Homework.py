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


# Task 3. My dict
#
# class MyDict(dict):
#     def get(self, __key, __default=0):
#         return super().get(__key, __default)
#
#
# my_dict = MyDict()
# my_dict.setdefault(1, 2)
# print(my_dict.get(2))


# Task 4. Company
#
# class Person:
#     """
#     Basic class. Define person's parameters like (name, surname, age)
#
#     Args:
#          name (str): name of a person
#          surname (str): surname of person
#          age (int): age of person
#     """
#
#     def __init__(self, name, surname, age):
#         self.__name = name
#         self.__surname = surname
#         self.__age = age
#
#     def get_name(self):
#         """
#         Getter for name
#
#         :return: name
#         :rtype: str
#         """
#         return self.__name
#
#
# class Employee(Person):
#     """
#     class Employee. Parent: Person
#     """
#
#     def salary_calculate(self):
#         """method for salary calculating"""
#         pass
#
#
# class Manager(Employee):
#     """
#     class Manager. Parent: Employee
#
#     Args:
#         name (str): name of a person
#         surname (str): surname of person
#         age (int): age of person
#         salary (int): salary of employee
#     """
#
#     def __init__(self, name, surname, age, salary):
#         super().__init__(name, surname, age)
#         self.__salary = salary
#
#     def salary_calculate(self):
#         """salary calculating
#
#         :return: final salary for work
#         :rtype: int
#         """
#         print('Salary of manager {}: {}'.format(self.get_name(), self.get_salary()))
#         return self.get_salary()
#
#     def get_salary(self):
#         """
#         Getter for salary
#
#         :return: final salary for work
#         :rtype: int
#         """
#         return self.__salary
#
#
# class Agent(Employee):
#     """
#     class Agent. Parent: Employee
#
#     __salary: fix salary for agents
#
#     Args:
#         name (str): name of a person
#         surname (str): surname of person
#         age (int): age of person
#         volume_of_sales (int): volume of sales
#     """
#
#     __salary = 5000
#
#     def __init__(self, name, surname, age, volume_of_sales):
#         super().__init__(name, surname, age)
#         self.__volume_of_sales = volume_of_sales
#
#     def get_salary(self):
#         """
#         Getter for salary
#
#         :return: final salary for work
#         :rtype: int
#         """
#         return self.__salary
#
#     def get_volume_of_sales(self):
#         """
#         Getter for volume of sales
#
#         :return: volume of sales
#         :rtype: int
#         """
#         return self.__volume_of_sales
#
#     def salary_calculate(self):
#         """salary calculating
#
#         :return: final salary for work
#         :rtype: int
#         """
#         __res = self.get_salary() + (self.get_volume_of_sales() * 5 // 100)
#         print('Salary of agent {}: {}'.format(self.get_name(), __res))
#         return __res
#
#
# class Worker(Employee):
#     """
#       class Worker. Parent: Employee
#
#       Args:
#           name (str): name of a person
#           surname (str): surname of person
#           age (int): age of person
#           hours_worked (int): hours worked
#       """
#
#     def __init__(self, name, surname, age, hours_worked):
#         super().__init__(name, surname, age)
#         self.__hours_worked = hours_worked
#
#     def get_hours_worked(self):
#         """
#         Getter for worked hours
#
#         :return: total hours in work
#         :rtype: int
#         """
#         return self.__hours_worked
#
#     def salary_calculate(self):
#         """salary calculating
#
#         :return: final salary for work
#         :rtype: int
#         """
#         __res = 100 * self.get_hours_worked()
#         print('Salary of worker {}: {}'.format(self.get_name(), __res))
#         return __res
#
#
# manager1 = Manager(name='Oleg', surname='Tinkoff', age=55, salary=13000)
# manager2 = Manager(name='Alex', surname='Bolt', age=25, salary=13000)
# manager3 = Manager(name='Mihail', surname='Kormakov', age=34, salary=13000)
#
# agent1 = Agent(name='Victor', surname='Kabanov', age=49, volume_of_sales=15000)
# agent2 = Agent(name='Artem', surname='Aliev', age=29, volume_of_sales=9000)
# agent3 = Agent(name='Gena', surname='Sergeev', age=57, volume_of_sales=17000)
#
# worker1 = Worker(name='Gosha', surname='Cucenko', age=18, hours_worked=120)
# worker2 = Worker(name='Ivan', surname='Pavlov', age=21, hours_worked=180)
# worker3 = Worker(name='Stepan', surname='Lamodin', age=61, hours_worked=190)
#
# employees_list = [manager1, manager2, manager3, agent1, agent2, agent3, worker1, worker2, worker3]
# total_salary = 0
# for employee in employees_list:
#     total_salary += employee.salary_calculate()
#
# print()
# print('Total salary of employees: {}'.format(total_salary))
