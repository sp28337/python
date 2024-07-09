# Task 1. Work with file 2
# import os
# import _io
#
#
# class File:
#     """
#     Context manager
#
#     May open file for reading, writing and adding data into it.
#     If file does not exist - creating new file in writing mode
#
#     Args:
#         name (str): file name
#         mode (str): mode
#
#     Attributes:
#           self._path (str): path to file
#
#     """
#     def __init__(self, name: str, mode='r') -> None:
#         self._name = name
#         self._mode = mode
#         self._path = os.path.abspath(self._name)
#
#     @property
#     def name(self) -> str:
#         """ Getter for file name"""
#         return self._name
#
#     @property
#     def mode(self) -> str:
#         """ Getter for mode"""
#         return self._mode
#
#     def __enter__(self):
#         if os.path.exists(self._path):
#             return _io.open(self._path, self._mode, encoding='utf-8')
#         else:
#             return _io.open(self._path, 'x', encoding='utf-8')
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         if exc_type is OSError:
#             return True
#         return False
#
#
# with File('test1.txt', 'w') as file:
#     print(file.name)
#     file.write('I gonna visit Thai very soon!')
#     print(file.mode)


# Task 2. Math module
# from typing import Union
#
#
# class MyMath:
#     """
#     Mathematics class
#
#     Contain functions for calculating:
#     - sphere surface area
#     - volume of cube
#     - circle area
#     - circle length
#     """
#     _PI = 3.14159265359
#
#     @property
#     def pi(self) -> float:
#         """ Getter pi constant """
#         return self._PI
#
#     @classmethod
#     def circle_len(cls, radius: int) -> Union[float, int]:
#         """
#         Contain formula fo calculating length of a circle
#
#         Args:
#             radius (int): radius of a circle
#         """
#         result = 2 * cls._PI * radius
#         return result
#
#     @classmethod
#     def circle_sq(cls, radius: int) -> Union[float, int]:
#         """
#         Contain formula fo calculating area of a circle
#
#         Args:
#             radius (int): radius of a circle
#         """
#         result = cls._PI * radius ** 2
#         return result
#
#     @classmethod
#     def sphere_sq(cls, radius: int) -> Union[int, float]:
#         """
#         Contain formula fo calculating area of a sphere
#
#         Args:
#             radius (int): radius of a sphere
#         """
#         result = 4 * cls._PI * radius ** 2
#         return result
#
#     @classmethod
#     def cub_vol(cls, side_len: int) -> Union[int, float]:
#         """
#         Contain formula fo calculating volume of a cube
#
#         Args:
#             side_len (int): length of a cube
#         """
#         result = side_len ** 3
#         return result
#
#
# res_1 = MyMath.circle_len(5)
# res_2 = MyMath.circle_sq(6)
# res_3 = MyMath.cub_vol(4)
# res_4 = MyMath.sphere_sq(6)
# print(res_1)
# print(res_2)
# print(res_3)
# print(res_4)
