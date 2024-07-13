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


# Task 3. 3D Modeling
# import math
# from typing import Any
#
#
# class Square2D:
#     """
#     Base class Square2D creates a square figure
#
#     Args:
#         side (int): length of a square
#     """
#
#     @classmethod
#     def verify_integer(cls, val: Any) -> None:
#         """
#         Integer verifier
#
#         :raise TypeError: if val is not an integer
#
#         """
#         if type(val) is not int:
#             raise TypeError('side must be an integer')
#
#     def __init__(self, side: int) -> None:
#         self.verify_integer(side)
#         self.side = side
#
#     @property
#     def side(self) -> int:
#         """ Getter for side """
#         return self._side
#
#     @side.setter
#     def side(self, side: int) -> None:
#         """
#         Setter for side
#
#         :param side: length of side
#         :type side: int
#         """
#
#         self._side = side
#
#     def perimetr(self) -> int:
#         """ Find perimeter of a square """
#         return self.side * 4
#
#     def area(self) -> int:
#         """ Find area of a square """
#         return self.side ** 2
#
#
# class Triangle2D:
#     """
#     Base class Triangle2D creates a triangle figure
#
#     Args:
#         base (int): base of a triangle
#         height (int): height of a triangle
#
#     """
#
#     @classmethod
#     def verify_integer(cls, val: Any) -> None:
#         """
#         Integer verifier
#
#         :raise TypeError: if val is not an integer
#
#         """
#         if type(val) is not int:
#             raise TypeError('val must be an integer')
#
#     def __init__(self, base: int, height: int) -> None:
#         self.verify_integer(base)
#         self.verify_integer(height)
#         self.base = base
#         self.height = height
#
#     @property
#     def base(self) -> int:
#         """ Getter for base """
#         return self._base
#
#     @base.setter
#     def base(self, val: int) -> None:
#         """
#         Setter for base
#
#         :param val: length of new base
#         :type val: int
#         """
#
#         self._base = val
#
#     @property
#     def height(self) -> int:
#         """ Getter for height """
#         return self._height
#
#     @height.setter
#     def height(self, val: int) -> None:
#         """
#         Setter for height
#
#         :param val: length of new height
#         :type val: int
#         """
#
#         self._height = val
#
#     def perimetr(self):
#         """
#         Find perimeter of a triangle
#
#         side_b (int): apothem
#
#         """
#         side_b = int(math.sqrt(self.height ** 2 + (self.base * 1 / 2) ** 2))
#         return side_b * 2 + self.base
#
#     def area(self) -> int:
#         """ Find area of a triangle """
#         return (self.base * self.height) // 2
#
#
# class Cube3D(Square2D):
#     """
#     class Cube3D represents a cube figure. Parent: Square3D
#
#     _surface (list): surface of cube
#
#     """
#     def __init__(self, side) -> None:
#         super().__init__(side)
#         self._surface = [Square2D for _ in range(6)]
#
#     @property
#     def surface(self) -> list:
#         """ Getter for surface """
#         return self._surface
#
#     def surf_area(self) -> int:
#         """ Calculate surface area of cube """
#         return self.area() * 6
#
#
# class Pyramid3D(Triangle2D):
#     """
#     class Pyramid3D represents a pyramid figure. Parent: Triangle2D
#
#     _surface (list): surface of triangle
#
#     """
#
#     def __init__(self, base, height) -> None:
#         super().__init__(base, height)
#         self._surface = [Triangle2D for _ in range(4)] + [Square2D]
#
#     @property
#     def surface(self) -> list:
#         """ Getter for surface """
#         return self._surface
#
#     def surf_area(self) -> int:
#         """
#         Calculate surface area of triangle
#
#         l (int): inclined height of pyramid
#         s (int): area of pyramid
#
#         """
#         l = int(math.sqrt(self.height ** 2 + (self.base / 2) ** 2))
#         print(l)
#         s = int(1 / 2 * self.perimetr() * l)
#         return s
#
#
# square = Square2D(3)
# cube = Cube3D(5)
# print(cube.surf_area())
#
# pyramid = Pyramid3D(5, 10)
# print(pyramid.perimetr())
# print(pyramid.surf_area())
# print(pyramid.__dict__)
# print(pyramid.surface)
# print(cube.surf_area())
