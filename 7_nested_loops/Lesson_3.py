# height = int(input('What height? '))
# width = int(input('What width? '))
# for i in range(width):
#     for j in range(height):
#         if i == 0:
#             print('_', end='')
#         elif j == 0 or j == height - 1:
#             print('|', end='')
#         else:
#             print(end=' ')
#     print()


# for i in range(20):
#     for j in range(50):
#         if j == 50 // 2 - 1:
#             print('|', end='')
#         elif j == 19 - i:
#             print('/', end='')
#         elif j == 29 + i:
#             print('\\', end='')
#         elif i == 20 // 2 - 1:
#             print('-', end='')
#         else:
#             print(end=' ')
#     print()


# size = int(input('Enter matrix size: '))
# for i in range(size):
#     for j in range(1, size + 1):
#         if j == size - i:
#             print(1, end='\t')
#         elif j > size - i:
#             print(2, end='\t')
#         else:
#             print(0, end='\t')
#     print()