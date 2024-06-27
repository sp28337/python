# Task 1. Endless iterator
#
# class CountIterator:
#     __counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__counter += 1
#         return self.__counter
#
#
# my_iter = CountIterator()
# for i in my_iter:
#     print(i)


# Task 2. Random summ
#
# import random
#
#
# class Iterator:
#
#     def __init__(self, limit):
#         self.first_elem = random.uniform(0, 1)
#         self.limit = limit
#         self.counter = 0
#
#     def __iter__(self):
#         self.first_elem = random.uniform(0, 1)
#         self.counter = 0
#         return self
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             self.first_elem += random.uniform(0, 1)
#             return round(self.first_elem, 2)
#         else:
#             raise StopIteration
#
#
# elements = int(input('Count of elements: '))
# print('Iterator elements:')
# iterator = Iterator(limit=elements)
#
# for element in iterator:
#     print(element)


# Task 3. Primes
#
# import math
#
#
# class Primes:
#     def __init__(self, limit):
#         self.limit = limit
#         self.num = 1
#
#     def __iter__(self):
#         self.num = 1
#         return self
#
#     def __next__(self):
#         self.num += 1
#         while self.num <= self.limit:
#             if self.is_prime(self.num):
#                 return self.num
#             self.num += 1
#         else:
#             raise StopIteration
#
#     @staticmethod
#     def is_prime(val):
#         for i in range(2, int(math.sqrt(val)) + 1):
#             if val % i == 0:
#                 return False
#         else:
#             return True
#
#
# prime_nums = Primes(limit=50)
# for i in prime_nums:
#     print(i, end=' ')
#
# print()
#
# for j in prime_nums:
#     print(j, end=' ')
