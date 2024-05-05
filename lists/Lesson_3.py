# text = input('Enter text: ')
# count = index = 0
# sym_list = list(text)
# for i in text:
#     if i == ':':
#         sym_list[index] = ';'
#         count += 1
#     index += 1
#
# for j in sym_list:
#     print(j, end='')
# print(count)


# text = input('Enter the string: ')
# sym_num = int(input('Enter number of the sym: '))
# print(f"Left sym: {text[sym_num - 2]}\nRight sym: {text[sym_num]}")
# if text[sym_num - 2] == text[sym_num - 1] and text[sym_num] == text[sym_num - 1]:
#     print('Symbols are equal')
# elif text[sym_num - 2] == text[sym_num - 1] or text[sym_num] == text[sym_num - 1]:
#     print('There are one equal symbol is')
# else:
#     print('There are not equal symbols')


# words = []
# count = [0, 0, 0]
# for i in range(3):
#     print(f"Enter {i + 1} word: ")
#     word = input()
#     words.append(word)
#
# text = input('Enter word from text: ')
# while text != 'end':
#     for j in range(3):
#         if text == words[j]:
#             count[j] += 1
#     text = input('Enter word from text: ')
# print('Count of words in text\n')
# for g in range(3):
#     print(words[g], ":", count[g])
