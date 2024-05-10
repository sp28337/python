# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
#
# print(main)
# print(f"Count of uncompleted tasks: {main.count(0)}")


# first_str = input('Enter first letter: ')
# second_str = input('Enter second letter: ')
#
# str1 = list(first_str).count('!')
# str2 = list(second_str).count('?')
# if str1 > str2:
#     print(first_str + second_str)
# elif str2 > str1:
#     print(second_str + first_str)
# else:
#     print('Wtf')


# pack = []
# decode = []
# last_p = 0
# packages = int(input('Enter count of packages: '))
# for i in range(1, packages + 1):
#     print(f"Package number {i}")
#     for j in range(4):
#         print(j + 1, 'bit:', end=' ')
#         bit = int(input())
#         pack.append(bit)
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Lots errors in the package!')
#         pack = []
#         last_p += 1
#     print()
#
# print(decode)
# print(f"Errors: {decode.count(-1)}")
# print(f"Lost packages: {last_p}")

