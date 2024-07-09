# Task 1. Work with file
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
