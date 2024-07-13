# Task 1. Transport
# from abc import ABC, abstractmethod
#
#
# class TransportPark(ABC):
#     """
#     Abstract base class for transport
#
#     Args:
#     color (str): color of transport
#     speed (int): speed of transport
#     """
#
#     def __init__(self, color: str, speed: int = 0) -> None:
#         self.__color = color
#         self.__speed = speed
#
#     @abstractmethod
#     def move(self) -> None:
#         """Any transport may move"""
#         pass
#
#     @abstractmethod
#     def signal(self) -> None:
#         """Any transport may do signal"""
#         pass
#
#     def get_color(self):
#         return self.__color
#
#     def get_speed(self):
#         return self.__speed
#
#
# class AudioPlayerMixin:
#     """
#     Mixin class for additional feature as an audio system
#
#     Attributes:
#     music_on (bool): Audio system status (default: False)
#     """
#     __music_on: bool = False
#
#     def audio_on(self) -> str:
#         """
#         Turn audio player ON
#
#         :return: result of this action
#         :rtype: str
#         """
#         self.__music_on = True
#         return 'Audio player is on'
#
#     def audio_off(self) -> str:
#         """
#         Turn audio player OFF
#
#         :return: result of this action
#         :rtype: str
#         """
#         self.__music_on = False
#         return 'Audio player is off'
#
#
# class Car(TransportPark):
#     """
#     Class Car. Parent: TransportPark
#
#     Args:
#     color (str): color of transport
#     speed (int): speed of transport
#     ttype (str): mark of the car
#     """
#
#     def __init__(self, color: str, ttype: str, speed: int = 0) -> None:
#         super().__init__(color, speed)
#         self.__ttype = ttype
#
#     def __str__(self) -> str:
#         return 'This is the {color} {ttype}'.format(color=self.get_color(), ttype=self.__ttype)
#
#     def move(self, way_to_move='ground') -> str:
#         """
#         Do move
#
#         :param way_to_move: area for moving
#         :type way_to_move: str
#         :return: result of this action
#         :rtype: str
#         """
#         if way_to_move == 'ground':
#             self.__speed = 60
#             return 'the car is driving now\nspeed: {} km/h'.format(self.__speed)
#         else:
#             return 'the car may drive only on ground!'
#
#     def signal(self) -> str:
#         return 'Boo!'
#
#
# class Boat(TransportPark):
#     """
#     Class boat. Parent TransportPark
#
#     Args:
#     color (str): color of transport
#     speed (int): speed of transport
#     name (str): name of the boat
#     """
#     def __init__(self, color: str, speed: int, name: str) -> None:
#         super().__init__(color, speed)
#         self.__name = name
#
#     def __str__(self) -> str:
#         return 'This is the {color} {name} boat'.format(color=self.__color, name=self.__name)
#
#     def move(self, way_to_move='water') -> str:
#         if way_to_move == 'water':
#             self.__speed = 70
#             return 'the boat went into the sea\nspeed: {} km/h'.format(self.__speed)
#         else:
#             return 'the boat may move only on water!'
#
#     def signal(self) -> str:
#         return 'Bam!'
#
#
# class Amphibian(TransportPark, AudioPlayerMixin):
#
#     def __str__(self) -> str:
#         return 'This is the {color} amphibian'.format(color=self.__color)
#
#     def move(self, way_to_move: str = 'water') -> str:
#         """
#         Do move
#
#         :param way_to_move: area for moving
#         :type way_to_move: str
#         :return: result of this action
#         :rtype: str
#         """
#         if way_to_move == 'water':
#             self.__speed = 40
#             return 'the amphibian went into the sea\nspeed: {} km/h'.format(self.__speed)
#         else:
#             self.__speed = 60
#             return 'the amphibian is driving now\nspeed: {} km/h'.format(self.__speed)
#
#     def signal(self) -> str:
#         return 'Bim!'
#
#
# sport_car = Car(color='red', ttype='Ford')
# amph = Amphibian('blue')
# print(sport_car)
# print(sport_car.move())
# print(amph.move())
# print(sport_car.move())


# Task 2. Figures
# from abc import ABC, abstractmethod
#
#
# class Figure(ABC):
#     """
#     Abstract class for making a figure
#
#     Args:
#         x (int): X coordinate
#         y (int): Y coordinate
#         length (int): length value
#         width (int): width value
#     """
#
#     def __init__(self, x: int, y: int, length: int, width: int) -> None:
#         self.__x = x
#         self.__y = y
#         self.__length = length
#         self.__width = width
#
#     @abstractmethod
#     def move(self, new_x: int, new_y: int) -> None:
#         """
#         Abstract method for setting new coordinates
#
#         :param new_x: new X coordinate
#         :param new_y: new Y coordinate
#         """
#         self.__x = new_x
#         self.__y = new_y
#         print('new coordinates of a figure: ({}, {})'.format(self.__x, self.__y))
#
#     def set_size(self, new_length: int, new_width: int):
#         """
#         <set_size> method for setting new size of a figure
#
#         :param new_length: new length size
#         :type new_length: int
#         :param new_width: new width size
#         :type new_width: int
#         """
#         self.__length = new_length
#         self.__width = new_width
#
#     def get_x(self):
#         """
#         Getter for X coordinate
#
#         :return: __x
#         :rtype: int
#         """
#         return self.__x
#
#     def get_y(self):
#         """
#         Getter for Y coordinate
#
#         :return: __y
#         :rtype: int
#         """
#         return self.__y
#
#     def get_length(self):
#         """
#         Getter for length of a figure
#
#         :return: __length
#         :rtype: int
#         """
#         return self.__length
#
#     def get_width(self):
#         """
#          Getter for width of a figure
#
#          :return: __width
#          :rtype: int
#          """
#         return self.__width
#
#
# class ResizeMixin:
#     """
#     Mixin class for changing size of a figure
#
#     """
#     def resize(self, new_length: int, new_width: int) -> None:
#         """
#         Calling <set_size> method from Figure(ABS) class
#
#         :param new_length: new length size
#         :type new_length: int
#         :param new_width: new width size
#         :type new_width: int
#         """
#         self.set_size(new_length, new_width)
#
#
# class Rectangle(Figure, ResizeMixin):
#     """
#     Rectangle class. Parents: Figure, ResizeMixin
#
#     """
#     def __str__(self) -> str:
#         return ('\nThis is rectangle\n'
#                 'coordinates: ({x}, {y})\n'
#                 'length: {l}\n'
#                 'width: {w}\n').format(x=self.get_x(),
#                                        y=self.get_y(),
#                                        l=self.get_length(),
#                                        w=self.get_width())
#
#     def move(self, new_x: int, new_y: int) -> None:
#         """
#           Abstract method for setting new coordinates
#
#           :param new_x: new X coordinate
#           :param new_y: new Y coordinate
#           """
#         super().move(new_x, new_y)
#
#
# class Square(Figure, ResizeMixin):
#     """
#     Square class. Parents: Figure, ResizeMixin
#
#     Args:
#         x (int): X coordinate
#         y (int): Y coordinate
#         size (int): Size of a square
#     """
#
#     def __init__(self, x: int, y: int, size: int) -> None:
#         super().__init__(x, y, size, size)
#         self.__size = size
#
#     def __str__(self) -> str:
#         """
#         Class representation
#
#         :return: x, y, size of the current class for information
#         :rtype: str
#         """
#         return ('\nThis is square\n'
#                 'coordinates: ({x}, {y})\n'
#                 'size: {s}\n').format(x=self.get_x(),
#                                       y=self.get_y(),
#                                       s=self.get_length())
#
#     def move(self, new_x: int, new_y: int) -> None:
#         """
#          Abstract method for setting new coordinates
#
#          :param new_x: new X coordinate
#          :param new_y: new Y coordinate
#          """
#         super().move(new_x, new_y)
#
#
# rectangle1 = Rectangle(x=10, y=20, length=5, width=6)
# rectangle2 = Rectangle(x=30, y=40, length=10, width=11)
# square_1 = Square(x=50, y=70, size=7)
#
# print(square_1)
# square_1.resize(20, 20)
# print(square_1)
#
# print(rectangle2)
# rectangle2.resize(1, 2)
# print(rectangle2)
#
# for figure in [rectangle1, rectangle2, square_1]:
#     print(figure)
#     figure.move(20, 30)
#     print(figure)
