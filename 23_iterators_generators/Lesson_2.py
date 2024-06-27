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
