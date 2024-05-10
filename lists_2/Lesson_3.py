# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in matrix:
#     for j in i:
#         print(j, end=' ')
#     print()


# total_list = []
# members = int(input('How many members in the competition?: '))
# team = int(input('How much people in a team?: '))
# if members % team != 0:
#     print('Error!')
# else:
#     member = 1
#     for i in range(1, members // team + 1):
#         list_teams = list(range(member, member + team))
#         total_list.append(list_teams)
#         member += team
#     print(total_list)


# goods = [['apples', 50], ['oranges', 190], ['mango', 100], ['limon', 200], ['bananas', 77]]
# new_good = []
# print(goods)
# fruit_name = input('Enter new fruit: ')
# price = int(input('Enter price of fruit: '))
# new_good.append(fruit_name)
# new_good.append(price)
# goods.append(new_good)
# print(goods)
# for i in range(len(goods)):
#     goods[i][1] = goods[i][1] + goods[i][1] * 8 / 100
#
# print(goods)