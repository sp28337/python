# Task 1. Stocks
#
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# big_storage.update(small_storage)
#
# goods_name = input("Enter good's name: ")
# if big_storage.get(goods_name):
#     print(big_storage.get(goods_name))
# else:
#     print('Error: there are not such position like that.')


# Task 2. Fruit crisis
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# print('Total profit: {0}'.format(sum(incomes.values())))
# min_value = list(incomes.values())
# min_key = list(incomes.keys())
# deleted_fruit = min_key[min_value.index(min(min_value))]
# print('Smallest profit from {0}. It contains {1} dollars'.format(deleted_fruit, min(min_value)))
# incomes.pop(deleted_fruit)
# print('Final dictionary:', incomes)


# Task 3. Frequency histogram
#
# def hist(string):
#     text_dict = dict()
#     for i in sorted(string):
#         text_dict[i] = string.count(i)
#     return text_dict
#
#
# text = input('Enter the text: ')
# hist_dict = hist(text)
#
# for i in hist_dict.keys():
#     print(i, ':', hist_dict[i])
#
# print('Maximum hist: {}'.format(max(hist_dict.values())))
