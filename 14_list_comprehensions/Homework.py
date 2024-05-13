# def text_analis(text):
#     letters = ['а', "е", "и", "о", "у", "э", "ю", "я", "ы"]
#     seek_letters = []
#     for i in text:
#         for j in letters:
#             if i == j:
#                 seek_letters.append(i)
#     return seek_letters
#
#
# user_text = input('Enter text: ')
#
# print(text_analis(user_text))
#
# print(f"Length of list: {len(text_analis(user_text))}")


# length = int(input('Enter length of the list: '))
# new_list = [(1 if x % 2 == 0 else x % 5) for x in range(10)]
# print(new_list)


# import random
#
# team_1 = [round(random.triangular(5, 10), 2) for x in range(20)]
# team_2 = [round(random.triangular(5, 10), 2) for x in range(20)]
# team_3 = [(team_1[x] if team_1[x] > team_2[x] else team_2[x]) for x in range(len(team_1))]
#
# print('First team:', team_1)
# print('Second team:', team_2)
# print('Winners of the competition:', team_3)


# alphabet = 'abcdefg'
# alphabet_copy = alphabet[:]
# print(alphabet_copy)
# print(alphabet[::-1])
# print(alphabet[::2])
# print(alphabet[1::2])
# print(alphabet[:1])
# print(alphabet[-1:-2:-1])
# print(alphabet[3:4])
# print(alphabet[-3:])
# print(alphabet[3:5])
# print(alphabet[4:2:-1])


# text = input('Enter the text: ')
# first = text.index('h')
# end = text[::-1].index('h')
# print(text[-end - 2:first:-1])


# def zero_to_end(arr):
#     right = 0
#     for left in range(len(arr)):
#         if arr[left] != 0:
#             arr[right], arr[left] = arr[left], arr[right]
#             right += 1
#     return arr
#
#
# numbers = [0, 1, -5, 9, 0, 84, -18, 0, 420, -23]
# print(zero_to_end(numbers))


# def move_zero_to_end(arr):
#     place_index = 0
#     for num in arr:
#         if num != 0:
#             arr[place_index] = num
#             place_index += 1
#     while place_index < len(arr):
#         arr[place_index] = 0
#         place_index += 1
#     return arr
#
# numbers = [0, 1, -5, 9, 0, 84, -18, 0, 420, -23]
# print(move_zero_to_end(numbers))


# def move_zero_to_end(arr):
#     zero_count = arr.count(0)
#     non_zero = [x for x in arr if x != 0]
#     return non_zero + [0] * zero_count
#
#
# numbers = [0, 1, -5, 9, 0, 84, -18, 0, 420, -23]
# print(move_zero_to_end(numbers))


# result = [[i + j for j in range(0, 9, 4)] for i in range(1, 5)]
# print(result)


# import random
# sticks = ['I' for stick in range(1, int(input('Count of sticks: ')) + 1)]
#
# for throw in range(1, int(input('Count of throws: ')) + 1):
#     right = random.randint(1, len(sticks))
#     left = random.randint(1, right)
#     print(f"Throw {throw}. Sticks knocked off number {left} to number {right}")
#     for j in range(left, right + 1):
#         sticks[j - 1] = '.'
#
# for stick in sticks:
#     print(stick, end='')


# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# new_list = [nice_list[i][j][k]
#             for i in range(len(nice_list))
#             for j in range(len(nice_list[i]))
#             for k in range(len(nice_list[i][j]))]
#
# print(new_list)
# print(nice_list)


# def caesar_cipher(string, user_shift):
#     char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33]
#                   if sym != ' '
#                   else ' ') for sym in string]
#     new_str = ''
#     for i in char_list:
#         new_str += i
#     return  new_str
#
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# input_str = 'это питон'
# shift = 3
#
# output_str = caesar_cipher(input_str, shift)
#
# print(output_str)