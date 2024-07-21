# Task 1. One-string code
#
# numbers = input('Enter numbers: ').strip().split()
# print(sorted(map(lambda x: int(x), numbers)))


# Task 2. One-string code 2
#
# string = 'qWe456rtY'
# print(list(filter(lambda x: x if x.islower() else None, string)))


# Task 3. reduce function
# from functools import reduce
#
#
# def my_add(a, b):
#     result = a + b.count('was')
#     print(f"{a} + {b.count('was')} = {result}")
#     return result
#
#
# sentences = ["Nory was a Catholic", "because her was mother was a Catholic",
#              "and Nory’s mother was a Catholic",
#              "because her father was a Catholic", "and her father was a Catholic",
#              "because his mother was a Catholic",
#              "or had been"]
#
# print((reduce(my_add, sentences, 0)))
