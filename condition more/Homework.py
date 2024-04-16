# level = 1
# exp = int(input('Enter your experience: '))
# if 1000 <= exp < 2500:
#     level += 1
#     print('Your level is:', level)
# elif 2500 <= exp < 5000:
#     level += 2
#     print('Your level is:', level)
# elif exp >= 5000:
#     level += 3
#     print('Your level is:', level)


# num_1 = int(input('Enter 1 num: '))
# num_2 = int(input('Enter 2 num: '))
# num_3 = int(input('Enter 3 num: '))
# if num_1 > num_2 and num_1 > num_3:
#     print(num_1)
# elif num_2 > num_3:
#     print(num_1)
# else:
#     print(num_3)


# def y_func(x):
#     if x > 0:
#         y = x - 12
#         return print('Y =', y)
#     elif x < 0:
#         y = x ** 2
#         return print('Y =', y)
#     elif x == 0:
#         return print('Y = 5')
#
#
# xx = int(input('Enter X: '))
# print(y_func(xx))


# student_place = int(input('Enter student place: '))
# points = int(input('Enter your points: '))
# if student_place <= 10:
#     print('Congratulations! You are in!')
#     if points >= 290:
#         print('You got scholarships!')
#     elif points < 290:
#         print('But you have not enough points for scholarships')


# day = int(input('Enter a day: '))
# hours = int(input('Enter how much hours you need work: '))
# if day == 1:
#     print('Taday is monday\nNeed work:', hours)
# elif day == 2:
#     print('Taday is tuesday\nNeed work:', hours)
# elif day == 3:
#     print('Taday is wednesday\nNeed work:', hours)
# elif day == 4:
#     print('Taday is thursday\nNeed work:', hours)
# elif day == 5:
#     print('Taday is friday\nNeed work:', hours)
#     if hours < 2:
#         print('You can go home earlier!')
# elif day == 6:
#     print('Taday is saturday\nNeed work:', hours)
# elif day == 7:
#     print('Taday is sunday\nNeed work:', hours)


# clients = int(input('How much clients? '))
# sellers = int(input('How much sellers? '))
# salary = int(input('Salary of a seller: '))
# if clients / sellers > 4:
#     print('Too few sellers')
#     if salary < 20000:
#         salary += 2000
# else:
#     print('Sellers are enough')
# print('Salary of sellers:', salary)


# num = int(input('Enter the number: '))
# if 9 < num < 100:
#     print('Double digit number')
# else:
#     print('Number is not double digit number')


# first_num = int(input('Gess first number: '))
# second_num = int(input('Gess second number: '))
# if first_num % 2 == 0 or second_num % 2 == 0:
#     print('Children give sweets to the teacher')
# elif first_num % 2 != 0 and second_num % 2 != 0:
#     print('Teacher gives sweets to children')


# rating = int(input('Что получил по математике? '))
# if 2 <= rating <= 3:
#     print('Плохо. Марш учиться!')
# elif 4 <= rating <= 5:
#     print('Молодец! Можешь отдохнуть.')


# num = int(input('Enter the number: '))
# if 9 < num < 100 or -100 < num < -9:
#     print('Double digit number')
# else:
#     print('Number is not double digit number')


# num_1 = int(input('First number: '))
# num_2 = int(input('Second number: '))
# num_3 = int(input('Third number: '))
# if num_1 == num_2 and num_1 == num_3:
#     print('3')
# elif num_1 == num_2 or num_1 == num_3 or num_3 == num_2:
#     print('2')
# else:
#     print('0')


# count_machines = int(input('Count of machines: '))
# s = int(input('Enter S of room: '))
# if count_machines >= 5 and s >= 100:
#     print('Good! It is our stuff!')
# else:
#     print('We need keep looking')


# s = int(input('Enter S of room: '))
# cost = int(input('Enter cost of room: '))
# if s >= 100 and cost <= 10000000:
#     print('Room is feet')
# elif (80 <= s < 100) and cost <= 7000000:
#     print('Room is feet')
# else:
#     print('Room is not feet!')


# profit = int(input('Enter your profit: '))
# if profit < 10000:
#     tax = 13 * profit / 100
#     print(tax)
# elif 10000 <= profit < 50000:
#     tax = (20 * (profit - 10000) / 100) + (13 * 10000 / 100)
#     print(tax)
# elif profit >= 50000:
#     tax = (30 * (profit - 50000) / 100) + (20 * (50000 - 10000) / 100) + (13 * 10000 / 100)
#     print(tax)


# time = int(input('Enter work time(0-23): '))
# if (8 <= time < 10) or (12 <= time < 14) or (15 <= time < 18) or (20 <= time < 22):
#     print('You can take a parcel')
# else:
#     print('You cannot take a parcel')