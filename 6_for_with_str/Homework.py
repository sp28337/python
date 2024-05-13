# text = input('Enter text')
# count = 0
# for i in text:
#     count += 1
#     if i == '*':
#         print(count)


# rows = int(input('Number of rows: '))
# seats = int(input('Number of seats: '))
# meters = int(input('Meters between rows: '))
# for i in range(rows):
#     print('=' * seats, '*' * meters, '=' * seats)


# number = int(input('Enter the number: '))
# for i in range(number // 2 + 1):
#     print(i * 2, end=' ')
#     if i * 2 == number:
#         break
#     print(i * 2 + 1, end='\n')


# a, b = 8, 10
# while True:
#     print(f"Bally at point {a} and {b}")
#     move = input('Where to go? ')
#     if move == 'W' and a < 15:
#         a += 1
#     elif move == 'S' and 0 < a:
#         a -= 1
#     elif move == "A" and 0 < b:
#         b -= 1
#     elif move == "D" and b < 20:
#         b += 1


# text = input('Enter the text: ')
# for i in text:
#     if i != '*':
#        print(i, end='')


# name = input('Enter your full name: ')
# print('Second name: ', end='')
# for i in name:
#     print(i, end='')
#     if i == ' ':
#         print('\nName: ', end='')


# text = input('Enter text: ')
# last_s = ''
# count = 1
# max_seq = 0
# for i in text:
#     if i == last_s:
#         count += 1
#         max_seq = count
#     elif count >= max_seq:
#         max_seq = count
#         count = 1
#     last_s = i
# print('Longest sequence is', max_seq)


# text = input('Enter the text: ')
# length, max_word = 0, 0
# for i in text:
#     if i == ' ':
#         max_word = length
#         length = 0
#         continue
#     length += 1
# print(f"Length of biggest word: {max_word}")


# import time
# t1 = time.time()
# word = input('Enter a word: ')
# if word[0] == word[-1]:
#     print('Letters is equal')
# else:
#     print('Letters is not equal!')
# t2 = time.time()
# time = t2 - t1
# print(time)


# length = int(input('Enter length: '))
# symbol = int(input('How much symbols? '))
# print('~' * ((length - symbol) // 2) + '!' * symbol + '~' * ((length - symbol) // 2))


# count_milk = 0
# summ = 0
# text = input('Enter a/b letters: ')
# for i in text:
#     count_milk += 2
#     if i == 'b':
#         summ += count_milk
#     elif i == 'a':
#         continue
#     else:
#         print('Error')
# print(summ)


# text = input('Enter a text: ')
# words = text.split()
# print(len(words))


# word = input('Enter word to encode: ')                        task #15
# new_word = ''
# for i in word:
#     new_word += word[0]
#     word = word[1:]
#     word = word[::-1]
# print(new_word)
#
# word2 = input('Enter word to encode: ')
# part_1 = ''
# part_2 = ''
# for j in range(len(word2) // 2):
#     part_1 += word2[0]
#     part_2 += word2[1]
#     word2 = word2[2:]
# print(part_1 + part_2[::-1])
