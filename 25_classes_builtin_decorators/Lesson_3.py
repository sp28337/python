# Task 1. Work with file
# import os
# import _io
# import time
# from typing import Optional, Any
#
#
# class File:
#     """
#     Context manager
#     """
#
#     def __init__(self, name_file: str, mode: str, encoding: str = 'utf-8') -> None:
#         self.__name_file = name_file
#         self.__mode = mode
#         self.__encoding = encoding
#         self.__file = None
#         self.__start_time = None
#         print('- Initialization file {0}'.format(self.__name_file))
#
#     def __enter__(self) -> Optional[Any]:
#         __path = os.path.abspath(self.__name_file)
#         print('- opening file...\n')
#         if os.path.isfile(__path):
#             self.__start_time = time.time()
#             self.__file = open(self.__name_file, self.__mode)
#             return self.__file
#
#         else:
#             print('[!] File <{}> not found!'.format(self.__name_file))
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         if self.__file:
#             self.__file.close()
#             print('[?] Context manager was working for ({} sec)'.format(round(time.time() - self.__start_time, 4)))
#             print('\n- File {0} was closed'.format(self.__name_file))
#
#         if exc_type:
#             print('[!] Caught an exception <{0}>: {1}'.format(exc_type.__name__, exc_val))
#             return True
#
#
# with File('test.txt', 'r') as test_file:
#     result = test_file.read()
#     test_file.seek(0)
#     for i in test_file:
#         print(i)


# Task 2. Example
#
# class Example:
#     """ Context manager """
#     def __init__(self) -> None:
#         print('__init__ call')
#
#     def __enter__(self) -> None:
#         print('__enter__ call')
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         print('__exit__ call')
#         if exc_type:
#             print('Type error: {0}\n'
#                   'Value error: {1}\n'
#                   'Due to: {2}'.format(exc_type, exc_val, exc_tb)
#                   )
#         return True
#
#
# my_obj = Example()
# with my_obj as obj:
#     print('Код внутри первого вызова контекст менеджера')
#     with my_obj as obj2:
#         raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
#     print('Я обязательно выведусь...')
