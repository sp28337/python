# Task 1. Min and max
# from typing import Union, Dict, List
#
#
# grades: List[Dict[str, Union[str, int]]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41},
#                                             {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37},
#                                             {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
#                                             {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2},
#                                             {'name': 'Mary', 'score': 63},
#                                             {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44},
#                                             {'name': 'Richard', 'score': 78},
#                                             {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13},
#                                             {'name': 'Lloyd', 'score': 52},
#                                             {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40},
#                                             {'name': 'James', 'score': 54},
#                                             {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9},
#                                             {'name': 'Bruce', 'score': 68},
#                                             {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22},
#                                             {'name': 'Aaron', 'score': 3},
#                                             {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94},
#                                             {'name': 'Sandra', 'score': 40},
#                                             ]
#
# print(min(grades, key=lambda x: x['score']))
# print(max(grades, key=lambda x: x['score']))


# Task 2. Sorting
# from pprint import pprint
#
#
# class Person:
#     """
#     Class Person. Represents any person
#
#     Args:
#         name (str): person name
#         age (str): person age
#         country (str): living country
#
#      """
#
#     def __init__(self, name: str, age: str, country: str) -> None:
#         self.name = name
#         self.age = age
#         self.country = country
#
#     @property
#     def name(self) -> str:
#         """ Getter for name """
#         return self.__name
#
#     @name.setter
#     def name(self, new_name: str) -> None:
#         """ Setter for name """
#         self.__name = new_name
#
#     @property
#     def age(self) -> str:
#         """ Getter for age """
#         return self.__age
#
#     @age.setter
#     def age(self, new_age: str) -> None:
#         """ Setter for age """
#         self.__age = new_age
#
#     @property
#     def country(self) -> str:
#         """ Getter for country """
#         return self.__country
#
#     @country.setter
#     def country(self, new_country: str) -> None:
#         """ Setter for country """
#         self.__country = new_country
#
#
# def age_sort(string: str) -> int:
#     """ Getting age from full string of person """
#     age = ''
#     for sym in string:
#         if sym.isdigit():
#             age += sym
#     return int(age)
#
#
# user1 = Person('Ivan', '30', 'Russia')
# user2 = Person('Pavel', '29', 'Thailand')
# user3 = Person('Goga', '27', 'USA')
# user4 = Person('Nik', '55', 'Canada')
# user5 = Person('Artem', '18', 'Vologda')
#
# people_list = [' | '.join(usr.__dict__.values()) for usr in [user1, user2, user3, user4, user5]]
# #people_list = [''.join(usr.age) for usr in [user1, user2, user3, user4, user5]]
#
# print(type(people_list))
# pprint(people_list)
# print()
# pprint(sorted(people_list, key=lambda x: age_sort(x)))
# print()
# pprint(sorted(people_list, key=lambda x: age_sort(x), reverse=True))
