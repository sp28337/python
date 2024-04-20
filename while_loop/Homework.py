# till = int(input('Find power 3 for each digit from 1 to '))
# count = 1
# while count <= till:
#     print(count, '** 3 =', count ** 3)
#     count += 1


# seconds = int(input('How much seconds need to wait? '))
# while seconds >= 0:
#     print(seconds)
#     seconds -= 1


# name = input('What is your name? ')
# duty = int(input('Enter your duty: '))
# while True:
#     print(name, 'summ of your duty is', duty)
#     money = int(input('How much money do you wanna take in? '))
#     duty -= money
#     if duty <= 0:
#         print('Your duty was closed!')
#         break


# num = int(input('Enter the num: '))
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print(count)


# count = 0
# while True:
#     seq_num = int(input('Enter a number: '))
#     if seq_num == 0:
#         break
#     elif seq_num % 2 == 0:
#         count += 1
# print(count)


# ticket = int(input('Enter ticket number: '))
# t_1 = (ticket // 1000) % 10 + (ticket // 10000) % 10 + (ticket // 100000) % 10
# t_2 = ticket % 10 + (ticket // 10) % 10 + (ticket // 100) % 10
# if t_2 == t_1:
#     print('Ticket is HAPPY!!!')
# else:
#     print('Ticket is not happy')


# a = int(input('First member of progressy: '))
# b = int(input('Difference of progressy: '))
# n = int(input('How much members in progressy: '))
# summ = 0
# while n > 0:
#     summ += a
#     print(a)
#     a += b
#     n -= 1
# print('Summa of progressy =', summ)


# first_day = int(input('How much did you run in first day? '))
# need_run = int(input('How much do you want to run? '))
# day = 0
# while need_run > 0:
#     day += 1
#     need_run -= first_day
#     first_day += (10 * first_day / 100)
# print('Need days for get it -', day)


# count_plus = 0
# count_minus = 0
# while True:
#     feed_back = int(input('Enter your feedback: '))
#     if feed_back == 0:
#         break
#     elif feed_back > 0:
#         count_plus += 1
#     else:
#         count_minus += 1
# print('Count positive digits:', count_plus, '\nCount negative digits:', count_minus)


# print('8-hours work day started')
# hour = 0
# tasks = 0
# store = ''
# while hour < 8:
#     hour += 1
#     print(hour, 'hour')
#     tasks += int(input('How much tusks was solved by Maxim? '))
#     call_wife = int(input('Your wife is calling you! Take a phone? '))
#     if call_wife == 0:
#         continue
#     elif call_wife == 1:
#         store = 'Need go to the store'
# print('Work day finished. Total tasks were done:', tasks)
# print(store)


# seq_t = int(input('Enter temperature: '))
# max_t = 0
# while seq_t != 0:
#     if seq_t > max_t:
#         max_t = seq_t
#     seq_t = int(input('Enter temperature: '))
# print(max_t)


# bank = int(input('Enter bank count: '))
# year_tax = int(input('Year tax: '))
# count_we_need = int(input('How much count bank do you want to get? '))
# year = 0
# while bank < count_we_need:
#     year += 1
#     bank += (year_tax * bank / 100)
# print('You need', year, 'year to get', count_we_need, 'dollars in your bank count')


# number = int(input('Enter a number: '))
# count_tries = 1
# while number != 7:
#     count_tries += 1
#     if number > 7:
#         print('Number is more than need. Try  again!')
#     else:
#         print('Number is less than need. Try again!')
#     number = int(input('Enter a number: '))
# print('You guessed! Congratulations! Tries:', count_tries)


# start, finish, count = 1, 100, 0
# while True:
#     n = (start + finish) // 2
#     print('Your number is equal to, less than or greater than number', n, '?')
#     answer = int(input('1 - equal, 2 - less, 3 - more '))
#     count += 1
#     if answer == 1:
#         print('You win!')
#         break
#     elif answer == 2:
#         finish = n
#     elif answer == 3:
#         start = n
