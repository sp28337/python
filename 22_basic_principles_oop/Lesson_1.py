# Task 1. Point coordinates
#
# class Point:
#     __total_points = 0
#     __coordinates_set = set()
#
#     def __init__(self, x=0, y=0):
#         self.set_x(x)
#         self.set_y(y)
#         self.__number = Point.__total_points
#         if self.coordinates_exists(x, y):
#             raise ValueError(f'Point with coordinates ({x}, {y}) already exists!')
#         Point.__coordinates_set.add((x, y))
#         Point.__total_points += 1
#         print('(Point number {} initialized)'.format(self.__number))
#
#     def coordinates_exists(self, x, y):
#         return (x, y) in self.__coordinates_set
#
#     def __str__(self):
#         return '--> Point {n} info: ({x}, {y})'.format(n=self.__number, x=self.__x, y=self.__y)
#
#     def get_x(self):
#         return 'X = {}'.format(self.__x)
#
#     def get_y(self):
#         return 'Y = {}'.format(self.__y)
#
#     def set_x(self, x):
#         if isinstance(x, int):
#             self.__x = x
#         else:
#             raise ValueError('Incorrect type. X must be an integer!')
#
#     def set_y(self, y):
#         if isinstance(y, int):
#             self.__y = y
#         else:
#             raise ValueError('Incorrect type. X must be an integer!')
#
#
# try:
#     point1 = Point()
#     print(point1)
#     point2 = Point('b', 1)
#     print(point2)
#     print(point1.get_x())
#     print(point2.get_y())
# except ValueError as e:
#     print(e)
