# def selection_sort(my_list):
#     for i in range(len(my_list)):
#         for j in range(i, len(my_list)):
#             if my_list[j] < my_list[i]:
#                 my_list[j], my_list[i] = my_list[i], my_list[j]
# 
# 
# nums = [4, 9, 7, 6, 3, 2]
# selection_sort(nums)
# print(nums)
# 
# 
# import time
# start_time = time.time()
# 
# 
# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
# 
# 
# def selection(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         new_arr.append(arr.pop(smallest))
#     return new_arr
# 
# 
# print(selection([5, 3, 6, 2, 10, 4, 5, 7, 324, 5432, 5, 45, 547, -4, 3, 45, 65, 76, 564, 56, 65, ]))
# 
# 
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Время выполнения программы: {round(execution_time, 5)} секунд")