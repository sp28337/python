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
