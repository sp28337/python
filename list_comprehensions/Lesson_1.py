# def is_palindrome(new_list):                                  #TASK FROM PREVIOUS MODULE
#     rev_seq = []
#     for i in range(len(new_list) - 1, -1, -1):
#         rev_seq.append(new_list[i])
#     if new_list == rev_seq:
#         return True
#     else:
#         return False
#
#
# seq = []
# new_nums = []
# answer = []
#
# count_numbers = int(input('Enter count of numbers: '))
# for _ in range(count_numbers):
#     number = int(input('Enter the number: '))
#     seq.append(number)
#
# for i in range(0, len(seq)):
#     for j in range(i, len(seq)):
#         new_nums.append(seq[j])
#     if is_palindrome(new_nums):
#         for g in range(0, i):
#             answer.append(seq[g])
#         answer.reverse()
#         break
#     new_nums = []
#
# print(seq)
# print(f"Need numbers: {len(answer)}")
# print(f"List of numbers: {answer}")


# left_board = int(input('Enter left board: '))
# right_board = int(input('Enter right board: '))
#
# cubes = [x ** 3 for x in range(left_board, right_board + 1)]
# square = [x ** 2 for x in range(left_board, right_board + 1)]
#
# print(f"List of cubes in range from {left_board} to {right_board}: {cubes}")
# print(f"List of squares in range from {left_board} to {right_board}: {square}")


# text = input('Enter the string: ')
# symbol = input('Enter additional symbol: ')
#
# doubled_sym = [x * 2 for x in text]
# additional_sym = [x + symbol for x in doubled_sym]
# print(f"List of doubles symbols: {doubled_sym}\nSketch with additional symbol: {additional_sym}")


# def higher_price(price, percent):
#     return round(price * (1 + percent / 100), 2)
#
# prices_list = [float(input("Good's price: ")) for _ in range(5)]
#
# tax1 = int(input('Tax for first year: '))
# tax2 = int(input('Tax for second year: '))
#
#
# first_year = [higher_price(x, tax1) for x in prices_list]
# second_year = [higher_price(x, tax2) for x in prices_list]
#
# print(sum(prices_list), sum(first_year), sum(second_year))