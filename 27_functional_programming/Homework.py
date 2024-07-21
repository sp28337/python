# Task 1. New lists
# from functools import reduce
#
#
# floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
#
# names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
#
# numbers = [22, 33, 10, 6894, 11, 2, 1]
#
# floats2 = list(map(lambda x: round(x**3, 3), floats))
# names2 = list(filter(lambda x: x if len(x) >= 5 else None, names))
# numbers2 = reduce(lambda x, y: x * y, numbers)
#
# print(floats2)
# print(names2)
# print(numbers2)


# Task 2. <timeit> module
#
# import timeit
#
#
# gen_time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# lst_cmpr_time = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# map_time = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
#
# print(gen_time)
# print(lst_cmpr_time)
# print(map_time)
#
# # str1 = "-".join(str(n) for n in range(100))
# # str2 = "-".join([str(n) for n in range(100)])
# # str3 = "-".join(map(str, range(100)))
# #
# # print(str3)
# # print(str1)
# # print(str2)


# Task 3. ZIP again
# from typing import List
#
# strings: List[str] = ['a', 'b', 'c', 'd', 'e']
# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
# result = list(map(lambda x, y: (x, y), strings, numbers))
# print(result)


# Task 4. Code readability
# import timeit
#
# t1 = timeit.timeit("""def is_prime(num):
#     if num <= 1:
#         return False
#     for div in range(2, int(num ** 0.5) + 1):
#         if num % div == 0:
#             return False
#     return True
#
#
# print(*[x for x in range(1001) if is_prime(x)])""", number=10)
# print(t1)
#
# t2 = timeit.timeit("""print(*[n for n in range(2, 1001) if all(n % d != 0 for d in range(2, int(n**0.5) + 1))])""", number=10)
# print(t2)
#
# # def is_prime(num):
# #     if num <= 1:
# #         return False
# #     for div in range(2, int(num ** 0.5) + 1):
# #         if num % div == 0:
# #             return False
# #     return True
# #
# #
# # print(*[x for x in range(1001) if is_prime(x)])
#
# # print(*[n for n in range(2, 1001) if all(n % d != 0 for d in range(2, int(n**0.5) + 1))])


# Task 5. Palindrome come back
# from collections import Counter
#
#
# def can_be_palindrome(s):
#     return len(list(filter(lambda x: x % 2, Counter(s).values()))) <= 2
#
#     # s = ''.join(s.split()).lower()
#     # char_count = Counter(s)
#     # odd_count = 0
#     # for count in char_count.values():
#     #     if count % 2 != 0:
#     #         odd_count += 1
#     # return odd_count <= 1
#
#
# print(can_be_palindrome("A man a plan a canal Panama"))
# print(can_be_palindrome('ababc'))
# print(can_be_palindrome('abbbc'))
