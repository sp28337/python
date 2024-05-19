# Task 1. Making tuples
#
# import random
#
# tuple1 = tuple(random.randint(0, 5) for _ in range(10))
# tuple2 = tuple(random.randint(-5, 0) for _ in range(10))
# tuple3 = tuple1 + tuple2
# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple3.count(0))


# Task 2. Cylinder
#
# import math
#
#
# def find_side(r, h):
#     new_side = 2 * math.pi * r * h
#     s = math.pi * r ** 2
#     full = new_side + 2 * s
#     return new_side, full
#
#
# radius = float(input('Enter radius of cylinder: '))
# height = float(input('Enter height of cylinder: '))
#
# result = find_side(radius, height)
# for value in result:
#     print(round(value, 2))
#