# nums_list = []
# n = int(input('Кол-во чисел в списке: '))
# for _ in range(n):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
# maximum = nums_list[0]
# minimum = nums_list[0]
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#     if minimum >= i:
#         minimum = i
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)


# list_numbers = []
# numbers_in_list = int(input('Enter how many numbers will be in the list?: '))
# k_number = int(input('Enter K number: '))
# summ = 0
# for i in range(numbers_in_list):
#     add_number = int(input('Enter number: '))
#     list_numbers.append(add_number)
#     if add_number % k_number == 0:
#         summ += i
# print(summ)


# list_of_points = []
# dogs = int(input('How many dogs?: '))
# for i in range(dogs):
#     print(f"How many points for {i} dog?:", end=' ')
#     points = int(input())
#     list_of_points.append(points)
# print(list_of_points)
# maximum = list_of_points[0]
# minimum = list_of_points[0]
# for j in list_of_points:
#     if maximum < j:
#         maximum = j
#     if minimum >= j:
#         minimum = j
# for g in range(dogs):
#     if maximum == list_of_points[g]:
#         list_of_points[g] = minimum
#     elif minimum == list_of_points[g]:
#         list_of_points[g] = maximum
# print(list_of_points)

