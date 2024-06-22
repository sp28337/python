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


# Task 5. Car
#
# import math
#
#
# class Car:
#     """
#     Basic class. Define coordinates and direction of vehicle
#
#     Args:
#         x (int): x coordinate
#         y (int): y coordinate
#         angle (int): direction of vehicle in degrees
#     """
#     def __init__(self, x, y, angle):
#         self.__x = x
#         self.__y = y
#         self.__angle = angle
#
#     def __str__(self):
#         return ('Car\n'
#                 'coordinates: ({0}, {1})\n'
#                 'direction: {2} degree(s)\n').format(self.get_x(), self.get_y(), self.get_angle())
#
#     def set_x(self, number):
#         """
#         Setter for x coordinate
#
#         :param number: change <x> coordinate to number
#         :type number: int
#         """
#         self.__x = number
#
#     def set_y(self, number):
#         """
#         Setter for x coordinate
#
#         :param number: change <y> coordinate to number
#         :type number: int
#         """
#         self.__y = number
#
#     def set_angle(self, degrees):
#         """
#         Setter for angle
#
#         :param degrees: change direction of the vehicle
#         :type degrees: int
#         """
#         self.__angle = degrees
#
#     def get_x(self):
#         """
#         Getter for <x> coordinate
#
#         :return: value of <x> coordinate
#         :rtype: int
#         """
#         return self.__x
#
#     def get_y(self):
#         """
#         Getter for <y> coordinate
#
#         :return: value of <y> coordinate
#         :rtype: int
#         """
#         return self.__y
#
#     def get_angle(self):
#         """
#         Getter for angle
#
#         :return: direction of the vehicle
#         :rtype: int
#         """
#         return self.__angle
#
#     def change_direction(self, new_angle):
#         """
#         Set old direction to new direction
#
#         :param new_angle: new direction
#         :type new_angle: int
#         """
#         self.set_angle(new_angle)
#         print('New direction is {} degrees\n'.format(self.get_angle()))
#
#     def drive_to(self, a, b):
#         """
#         Vehicle drive to new destination
#
#         Attributes:
#             __distance (float): drove distance
#
#         :param a: new point on <x> coordinates
#         :param b: new point on <y> coordinates
#         :type a: int         :type b: int
#         """
#         __distance = round(math.sqrt(pow((a - self.get_x()), 2) + pow((b - self.get_y()), 2)), 2)
#         print('Car drove {} km\n'.format(__distance))
#         self.set_x(a)
#         self.set_y(b)
#
#
# class Bus(Car):
#     """
#     class Bus. Parent: Car
#
#     __ticket_price (int): price of ticket for one person
#
#     Args:
#         x (int): point on <x> coordinates
#         y (int): point on <y> coordinates
#         angle (int): direction of the vehicle
#         passengers (int): count of passengers in the bus
#         money (int): count of money
#     """
#
#     __ticket_price = 1
#
#     def __init__(self, x, y, angle, passengers=0, money=0):
#         super().__init__(x, y, angle)
#         self.__passengers = passengers
#         self.__money = money
#
#     def __str__(self):
#         info = super().__str__()
#         info = ''.join((info, 'type: Bus\n'
#                               'passengers: {}\n'
#                               'money: {}$\n'.format(self.get_passengers(), self.get_money()))
#                        )
#         return info
#
#     def set_passengers(self, count):
#         """
#         Setter for passengers
#
#         :param count: count of new passengers
#         :type count: int
#         """
#         self.__passengers = count
#
#     def set_money(self):
#         """
#         Setter for money.
#
#         Increases the amount of money depending on the ticket price and the number of passengers
#         """
#         self.__money += self.get_passengers() * self.get_ticket_price()
#         print('[+$] earned {}$'.format(self.get_money()))
#
#     def get_passengers(self):
#         """
#         Getter for passengers count
#
#         :return: count of passengers
#         :rtype: int
#         """
#         return self.__passengers
#
#     def get_money(self):
#         """
#         Getter for money count
#
#         :return: count of money
#         :rtype: int
#         """
#         return self.__money
#
#     def get_ticket_price(self):
#         """
#         Getter for price of a ticket
#
#         :return: price of one ticket
#         :rtype: int
#         """
#         return self.__ticket_price
#
#     def drive_to(self, a, b):
#         """
#         Vehicle drive to new destination and collects money for travel
#
#         Attributes:
#             __distance (float): drove distance
#
#         :param a: new point on <x> coordinates
#         :param b: new point on <y> coordinates
#         :type a: int         :type b: int
#         """
#         super().drive_to(a, b)
#         self.set_money()
#
#     def passenger_in(self, count=0):
#         """
#         A passenger comes inside. Set new passengers count
#
#         :param count: count of passengers (default = 0)
#         :type count: int
#         """
#         new_passengers = self.get_passengers() + count
#         self.set_passengers(new_passengers)
#         print('[+] {} passenger | total passengers: {}'.format(count, self.get_passengers()))
#
#     def passenger_out(self, count=0):
#         """
#         A passenger goes outside. Set new passengers count
#
#         :param count: count of passengers (default = 0)
#         :type count: int
#         """
#         new_passengers = self.get_passengers() - count
#         self.set_passengers(new_passengers)
#         print('[-] {} passenger | total passengers: {}'.format(count, self.get_passengers()))
#
#
# car = Car(5, 8, 45)
# print(car)
# car.drive_to(1, 3)
# print(car)
# car.change_direction(23)
# print(car)
#
# bus = Bus(1, 1, 33)
# print(bus)
# bus.passenger_in(7)
# bus.drive_to(2, 4)
# bus.passenger_out(2)
# bus.drive_to(4, 6)
# print(bus)


# Task 6. Cohabitation 2

import time
from random import randint


class House:
    __count_of_houses = 0

    def __init__(self, money=100, food=50, pet_food=30, dirt=0):
        self.__money = money
        self.__food = food
        self.__pet_food = pet_food
        self.__dirt = dirt
        self.set_count_of_houses()
        print('(House of number {0} initialized)'.format(self.get_count_of_houses()))

    def __str__(self):
        return 'House №{}'.format(self.get_count_of_houses())

    def info(self):
        return ('-*- HOUSE INFO -*-\n'
                'money: {0}\n'
                'food: {1}\n'
                'pet_food: {2}\n'
                'dirt: {3}\n').format(self.get_money(),
                                      self.get_food(),
                                      self.get_pet_food(),
                                      self.get_dirt())

    def get_count_of_houses(self):
        return self.__count_of_houses

    def get_money(self):
        return self.__money

    def get_food(self):
        return self.__food

    def get_pet_food(self):
        return self.__pet_food

    def get_dirt(self):
        return self.__dirt

    def set_dirt(self, val):
        if val > 0:
            self.__dirt += val
            print('  [-] --- it got more dirtier for {0}!'.format(val))
        elif val < 0:
            self.__dirt -= val
            print('  [+] -+- it became cleaner!'.format(val))
        else:
            self.__dirt = 0
            print('  [!] -|- everywhere cleand up!')
        print('dirt: {0}'.format(self.get_dirt()))

    def set_money(self, val):
        if val > 0:
            print('  [+] -+- husband earned {0}$!'.format(val))
            self.__money += val
        elif val < 0:
            print('  [-] -{0}$ someone waisting your money!'.format(val))
            self.__money -= val
        else:
            self.__money = 0
            print('  [!] -!- wallet is empty!')
        print('  money: {0}'.format(self.get_money()))

    def set_count_of_houses(self):
        self.__count_of_houses += 1

    def set_food(self, val):
        if val > 0:
            print('  [+] -+- someone put {0} food in the fridge'.format(val))
            self.__food += val
            print()
        elif val < 0:
            print('  [-] --- someone ate {0} food from the fridge'.format(val))
            self.__food -= val
            print()
        else:
            self.__food = 0
            print('  [!] -!- fridge is empty!')
        print('  food in fridge: {0}'.format(self.get_food()))

    def set_pet_food(self, val):
        if val > 0:
            print('  [+] -+- someone bought {0} food for pet'.format(val))
            self.__pet_food += val
            print()
        elif val < 0:
            print('  [-] --- cat ate {0} food'.format(val))
            self.__pet_food -= val
            print()
        else:
            self.__food = 0
            print('  [!] -!- Pet food is empty!')
        print('  pet food: {0}'.format(self.get_pet_food()))


class AliveObject:
    def __init__(self, name, home, fullness=30):
        self.__name = name
        self.__home = home
        self.__fullness = fullness

    def __str__(self):
        return ('[INFO] Name: {0} | Residence: {1}\n'
                'Fullness: {2}').format(self.get_name(), self.get_home(), self.get_fullness())

    def __del__(self):
        pass

    def get_name(self):
        return self.__name

    def get_home(self):
        return self.__home

    def get_fullness(self):
        return self.__fullness

    def set_fullness(self, val):
        if val > 0:
            print('  [+] -+- fullness rose + {0}'.format(val))
            self.__fullness += val
        elif val < 0:
            print('  [-] --- fullness down -{0}'.format(val))
            self.__fullness -= val
        print('  fullness: {0}'.format(self.get_fullness()))

    def check_fullness(self):
        if not self.get_fullness() >= 0:
            return self.__del__()
        elif 0 < self.get_fullness() < 10:
            print('[!] -!- DANGER level of fullness!\n{0}'.format(self.__str__()))


class People(AliveObject):
    def __init__(self, name, home, happiness=100):
        super().__init__(name, home)
        self.__happiness = happiness

    def __str__(self):
        info = super().__str__()
        new_info = '\n'.join((info, 'Happiness: {0}\n'.format(self.get_happiness())))
        return new_info

    def __del__(self):
        pass

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, val):
        if val > 0:
            self.__happiness += val
            print('  [+] -+- happiness up +{0}'.format(val))
        elif val < 0:
            self.__happiness -= val
            print('  [-] --- happiness down -{0}'.format(val))
        print('  happiness of {1}: {0}'.format(self.get_happiness(), self.get_name()))

    def pet_cat(self):
        print('\n[action] {0} is patting {1} ...'.format(self.get_name(), cat.get_name()))
        #time.sleep(1)
        self.set_happiness(5)
        self.set_fullness(-10)
        self.check_fullness()

    def eat(self):
        if self.get_home().get_food() >= 30:
            print('\n[action] {0} is eating...'.format(self.get_name()))
            #time.sleep(0.5)
            self.set_fullness(30)
            self.get_home().set_food(-30)
        elif 0 < self.get_home().get_food() < 30:
            print('\n[action] {0} is eating...'.format(self.get_name()))
            #time.sleep(0.5)
            self.set_fullness(self.get_home().get_food())
            self.get_home().set_food(0)
        else:
            print('\n[!] -!- {0} is hungry!'.format(self.get_name()))
            self.set_fullness(-10)
            self.check_fullness()
            self.check_happiness()

    def check_happiness(self):
        if not self.get_happiness() >= 10:
            return self.__del__()
        elif 10 < self.get_happiness() < 20:
            print('\n[!] -!- DANGER level! {1} has deep depression!\n'
                  '{0}\n'.format(self.__str__(), self.get_name()))

    def play(self):
        pass

    def go_work(self):
        pass


class Husband(People):
    def __del__(self):
        print('\n[*] {} dead!\n'.format(self.get_name()))

    def play(self):
        print('[action] {} playing computer...'.format(self.get_name()))
        #time.sleep(0.5)
        self.set_happiness(20)
        self.set_fullness(-10)
        self.check_fullness()
        self.check_happiness()

    def go_work(self):
        print('[action] {} is working...'.format(self.get_name()))
        #time.sleep(0.5)
        self.set_fullness(-10)
        self.check_fullness()
        self.check_happiness()


class Wife(People):
    def __del__(self):
        print('\n[*] {} dead!\n'.format(self.get_name()))

    def cleaning_up(self):
        print('[action] {} is cleaning up...'.format(self.get_name()))
        #time.sleep(0.5)
        self.get_home().set_dirt(-randint(80, 100))
        self.set_fullness(-10)
        self.check_fullness()
        self.check_happiness()

    def buy_fur_coat(self, count):
        if count > 0:
            print('[action] {} went for purchases...'.format(self.get_name()))
            #time.sleep(0.5)
            total_price = count * 350
            if self.get_home().get_money() >= total_price:
                print('[+] {0} bought {1} fur coat(s)!'.format(self.get_name(), count))
                self.get_home().set_money(-total_price)
                self.set_fullness(60)
            else:
                print('[!] Not enough money!')
                self.set_fullness(-10)
            self.check_fullness()
            self.check_happiness()
        else:
            raise ValueError('{} cannot buy 0 or less fur coat(s)!'.format(self.get_name()))

    def buy_food(self, count):
        if count > 0:
            print('[action] {} went for purchases...'.format(self.get_name()))
            #time.sleep(0.5)
            if self.get_home().get_money() >= count:
                print('[+] {0} bought {1} food!'.format(self.get_name(), count))
                self.get_home().set_money(-count)
            else:
                print('[!] Not enough money!')
        else:
            raise ValueError('{} cannot buy 0 or less food!'.format(self.get_name()))
        self.set_fullness(-10)
        self.check_fullness()
        self.check_happiness()


class Cat(AliveObject):
    def __del__(self):
        print('\n[*] {} dead!\n'.format(self.get_name()))

    def go_bed(self):
        print('[action] {0} is sleeping now...'.format(self.get_name()))
        #time.sleep(0.5)
        self.set_fullness(-10)
        self.check_fullness()

    def tear_up_wallpaper(self):
        print('[action] {0} is tearing wallpapers!'.format(self.get_name()))
        #time.sleep(0.5)
        self.get_home().set_dirt(-5)
        self.set_fullness(-10)
        self.check_fullness()

    def eat(self):
        if self.get_home().get_pet_food() >= 10:
            print('[action] {0} is eating food...'.format(self.get_name()))
            #time.sleep(0.5)
            self.set_fullness(20)
            self.get_home().set_pet_food(-20)
        elif 0 < self.get_home().get_pet_food() < 10:
            print('[action] {0} is eating food...'.format(self.get_name()))
            self.set_fullness(self.get_home().get_pet_food())
            self.get_home().set_pet_food(0)
        else:
            print('[!] {0} is hungry!'.format(self.get_name()))
            self.set_fullness(-5)
            self.check_fullness()


home1 = House()
husband = Husband('Artem', home1)
wife = Wife('Katya', home1)
cat = Cat('Cat', home1)
print(wife)

cat_actions = {0: 'go_bed()',
               1: 'tear_up_wallpaper()',
               2: 'eat()'
               }
husband_actions = {0: 'play()',
                   1: 'go_work()',
                   2: 'eat()',
                   3: 'pet_cat()'
                   }
wife_actions = {0: 'cleaning_up()',
                1: 'buy_fur_coat({})'.format(randint(1, 2)),
                2: 'eat()',
                3: 'buy_food({})'.format(randint(10, 100)),
                4: 'pet_cat()'
                }

days = 1
while days < 365:
    try:
        if home1.get_dirt() > 90:
            wife.set_happiness(-10)
            husband.set_happiness(-10)
        print(' *** Day {} ***'.format(days))
        for action in (husband, wife, cat):
            if action is husband:
                exec('{0}.{1}'.format('husband', husband_actions.get(randint(0, 3))))
            if action is wife:
                exec('{0}.{1}'.format('wife', wife_actions.get(randint(0, 4))))
            if action is cat:
                exec('{0}.{1}'.format('cat', cat_actions.get(randint(0, 2))))
        home1.set_dirt(5)
        days += 1
    except Exception as e:
        print(e)
else:
    print('\n*** SUCCESSFUL EXPERIMENT ***')
