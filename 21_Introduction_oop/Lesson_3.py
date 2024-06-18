# Task 1. Vehicle 3
#
# class Toyota:
#     def __init__(self, color, price, max_speed, current_speed):
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.current_speed = current_speed
#
#     def info(self):
#         print('Information\n'
#               'Color: {}\n'
#               'Price: {}\n'
#               'Max speed: {}\n'
#               'Current speed: {}\n'.format(self.color, self.price, self.max_speed, self.current_speed)
#               )
#
#     def set_current_speed(self, speed):
#         if speed > 0:
#             self.current_speed = speed
#         else:
#             print('Speed cannot be less than zero!')
#
#
# car1 = Toyota('Red', 1_000_000, 200, 0)
# car1.info()
# car1.set_current_speed(140)
# car1.info()


# Task 2. Point coordinates
#
# class Point:
#     total_points = 0
#     coordinates_set = set()
#
#     def __init__(self, x=0, y=0):
#         if self.coordinates_exists(x, y):
#             raise ValueError(f'Point with coordinates ({x}, {y}) already exists!')
#         Point.coordinates_set.add((x, y))
#         Point.total_points += 1
#         self.x, self.y, self.number = x, y, Point.total_points
#
#     def coordinates_exists(self, x, y):
#         return (x, y) in self.coordinates_set
#
#     def info(self):
#         print('Information about point number {n}\n'
#               'X = {x}\n'
#               'Y = {y}\n'
#               'Total points = {t}\n'.format(n=self.number,
#                                             x=self.x,
#                                             y=self.y,
#                                             t=self.total_points
#                                             )
#               )
#
#
# try:
#     point1 = Point()
#     point1.info()
#     point2 = Point()
#     point2.info()
# except ValueError as e:
#     print(e)


# Task 3. Happy farm
#
# class Potato:
#     states = {0: 'seedling', 1: 'crossbreed', 2: 'flowering', 3: 'ripe'}
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 3:
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):
#         print('Potato {} now {}'.format(self.index, Potato.states[self.state]))
#
#
# class PotatoGarden:
#
#     def __init__(self, count):
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print('Potato growing up!')
#         for i_potato in self.potatoes:
#             i_potato.grow()
#
#     def are_all_ripe(self):
#         if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
#             print('Potato does not ripe yet!\n')
#         else:
#             print('All potatoes is ripe!')
#
#
# my_garden = PotatoGarden(5)
# my_garden.are_all_ripe()
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()
