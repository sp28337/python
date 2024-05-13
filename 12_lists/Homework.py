# number = int(input('Enter the number: '))
# print(list(range(1, number + 1, 2)))


# names = ['Artem', 'Boris', 'Vlad', 'Gosha', 'Dima', 'Evgeniy', 'Genya', 'Zaxar']
# print(names[1::2])


# wrong_value = []
# cells = int(input('Enter count of cells: '))
# for i in range(cells):
#     print('Efficient of the cell', i + 1, ':', end=' ')
#     efficient = int(input())
#     if i > efficient:
#         wrong_value.append(efficient)
# for j in wrong_value:
#     print(j, end=' ')


# list_video_cards = []
# new_list_video_cards = []
# video_cards = int(input('How many video cards?: '))
# for i in range(1, video_cards + 1):
#     print(f"{i} Video card:", end=' ')
#     version = int(input())
#     list_video_cards.append(version)
#     if version < 3080:
#         new_list_video_cards.append(version)
# print(list_video_cards)
# print(new_list_video_cards)


# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
# 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# favorite = []
#
# movie = input('Enter the movie: ')
# while movie != 'end':
#     if movie in films:
#         favorite.append(movie)
#     else:
#         print('Error')
#     movie = input('Enter the movie: ')
# print(favorite)


# unique = 0
# word = input('Enter a word: ')
# words_list = list(word)
# for i in word:
#     if words_list.count(i) == 1:
#         unique += 1
# print(unique)


# containers_list = []
# total_containers = int(input('Total containers: '))
#
# for i in range(total_containers):
#     weight = int(input('Enter weight of the container: '))
#     containers_list.append(weight)
#
# new_container = int(input('Enter weight of the new container: '))
# for j in range(total_containers):
#     if new_container > containers_list[j]:
#         print(j + 1)
#         break
#     elif new_container == containers_list[j]:
#         print(j + 2)
#         break
# print(f"Number where new container will stay:")


# list_1 = [1, 4, -3, 0, 10]
# list_2 = []
# index = int(input('Enter index: '))
# for i in range(len(list_1)):
#     list_2.append(list_1[i - index])
# print(list_2)


# first_half = []
# second_half = []
# word = input('Enter a word: ')
# word_list = list(word)
# half = len(word) // 2
# for i in range(half):
#     first_half.append(word_list[i])
#     second_half.append(word_list[i - half])
# print(first_half)
# print(second_half)
# if first_half == second_half[::-1]:
#     print('Polindrom')
# else:
#     print('No')


# def bubbles(list_n):     #ПУЗЫРЬКОВАЯ СОРТИРОВКА
#     swap_boll = True
#     while swap_boll:
#         swap_boll = False
#         for i in range(len(list_n) - 1):
#             if list_n[i] > list_n[i + 1]:
#                 list_n[i], list_n[i + 1] = list_n[i + 1], list_n[i]
#                 swap_boll = True
#
#
# start_list = [1, 4, -3, 0, 10]
# bubbles(start_list)
# print(start_list)


# def insertion(list_nums):               #СОРТИРОВКА ВСТАВКАМИ
#     for i in range(1, len(list_nums)):
#         item = list_nums[i]
#         i2 = i - 1
#         while i2 >= 0 and list_nums[i2] > item:
#             list_nums[i2 + 1] = list_nums[i2]
#             i2 -= 1
#         list_nums[i2 + 1] = item
#
#
# nums = [54, 43, 3, 11, 0]
# insertion(nums)
# print(nums)


# def selection(sort_nums):                       #СОРТИРОВКА ВЫБОРКОЙ
#     for i in range(len(sort_nums)):
#         index = i
#         for j in range(i + 1, len(sort_nums)):
#             if sort_nums[j] < sort_nums[index]:
#                 index = j
#         sort_nums[i], sort_nums[index] = sort_nums[index], sort_nums[i]
#
#
# nums = [54, 43, 3, 11, 0]
# selection(nums)
# print(nums)


# def heapify(sort_nums, heap_size, root):                     #ПИРАМИДАЛЬНАЯ СОРТИРОВКА
#     l = root
#     left = (2 * root) + 1
#     right = (2 * root) + 2
#     if left < heap_size and sort_nums[left] > sort_nums[l]:
#         l = left
#     if right < heap_size and sort_nums[right] > sort_nums[l]:
#         l = right
#     if l != root:
#         sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
#         heapify(sort_nums, heap_size, l)
#
#
# def heap(sort_nums):
#     size = len(sort_nums)
#     for i in range(size, -1, -1):
#         heapify(sort_nums, size, i)
#     for i in range(size - 1, 0, -1):
#         sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
#         heapify(sort_nums, i, 0)
#
#
# nums = [54, 43, 3, 11, 0]
# heap(nums)
# print(nums)                    # Выведет [0, 3, 11, 43, 54]


# def mergeSort(sort_nums):                         #СОРТИРОВКА СЛИЯНИЕМ
#     if len(sort_nums) > 1:
#         mid = len(sort_nums) // 2
#         lefthalf = sort_nums[:mid]
#         righthalf = sort_nums[mid:]
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#         i = j = k = 0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 sort_nums[k] = lefthalf[i]
#                 i += 1
#             else:
#                 sort_nums[k] = righthalf[j]
#                 j += 1
#             k += 1
#         while i < len(lefthalf):
#             sort_nums[k] = lefthalf[i]
#             i += 1
#             k += 1
#         while j < len(righthalf):
#             sort_nums[k] = righthalf[j]
#             j += 1
#             k += 1
#
# nums = [54, 43, 3, 11, 0]
# mergeSort(nums)
# print(nums)


# def partition(sort_nums, begin, end):               #БЫСТРАЯ СОРТИРОВКА
#     part = begin
#     for i in range(begin+1, end+1):
#         if sort_nums[i] <= sort_nums[begin]:
#             part += 1
#             sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
#     sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
#     return part
#
#
# def quick_sort(sort_nums, begin=0, end=None):
#     if end is None:
#         end = len(sort_nums) - 1
#
#     def quick(sort_nums, begin, end):
#         if begin >= end:
#             return
#         part = partition(sort_nums, begin, end)
#         quick(sort_nums, begin, part-1)
#         quick(sort_nums, part+1, end)
#     return quick(sort_nums, begin, end)
#
#
# nums = [54, 43, 3, 11, 0]
# quick_sort(nums)
# print(nums) # Выведет [0, 3, 11, 43, 54]