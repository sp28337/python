# def summa(number):
#
#     summ = 0
#     for i in range(1, number + 1):
#         summ += i
#     print(f"\nI know that summa of numbers from 1 to {number} is {summ}")
#
#
# num = int(input('Enter the number: '))
# summa(num)


# def test():
#     number = int(input('Enter number: '))
#     if number >= 0:
#         positive()
#     else:
#         negative()
#
#
# def positive():
#     print('Positive')
#
#
# def negative():
#     print('Negative')
#
#
# test()


import math
def circle(r):
    s = math.pi * r ** 2
    print(f"Square of the circle is {s}")


# def rectangle(a, b):
#     s = a * b
#     print(f"Square of the rectangle is {s}")
#
#
# def triangle(a, b, angle):
#     s = 1 / 2 * a * b * math.sin(angle)
#     print(f"Square of the triangle is {s}")
#
#
# print('What area do you want to find? ')
# answer = input()
# if answer == 'circle':
#     radius = float(input('Enter the radius: '))
#     circle(radius)
# elif answer == 'rectangle':
#     a_side = float(input('Enter a side: '))
#     b_side = float(input('Enter b side: '))
#     rectangle(a_side, b_side)
# elif answer == 'triangle':
#     a_side = float(input('Enter a side: '))
#     b_side = float(input('Enter b side: '))
#     angle = int(input('Enter the angle: '))
#     triangle(a_side, b_side, angle)
# else:
#     print('Error!\n')


# def summa(n):
#     summ = 0
#     for i in range(1, n + 1):
#         summ += i
#     print('Summa digits of number', n, 'is', summ)
#     menu()
#
#
# def maximum(n):
#     max_n = 0
#     lust_n = n
#     while lust_n > 0:
#         if lust_n % 10 > max_n:
#             max_n = lust_n % 10
#         lust_n //= 10
#     print(f"Max digit in number {n} is {max_n}")
#     menu()
#
#
# def minimum(n):
#     min_n = 9
#     lust_n = n
#     while lust_n > 0:
#         if lust_n % 10 < min_n:
#             min_n = lust_n % 10
#         lust_n //= 10
#     print(f"Max digit in number {n} is {min_n}")
#     menu()
#
#
# def menu():
#     number = int(input('Enter the number: '))
#     to_do = input('What to do? ')
#     if to_do == 'summa':
#         summa(number)
#     elif to_do == 'maximum':
#         maximum(number)
#     elif to_do == 'minimum':
#         minimum(number)
#
#
# menu()


# def reverse(n):
#     print(int(n[::-1]))
#
#
# while True:
#     num = input('Enter the number: ')
#     if num == '0':
#         print('Program closed!')
#         break
#     reverse(num)


# def count_letters(t):
#     n = input('What kind digit do you wanna find? ')
#     l = input('What kind letter do you wanna find? ')
#     count_n = 0
#     count_l = 0
#     for i in t:
#         if i == n:
#             count_n += 1
#         elif i == l:
#             count_l += 1
#     print(f"\nCount of digits {n}: {count_n}\nCount of letters {l}: {count_l}")
#
#
# text = input('Enter the text: ')
#
# count_letters(text)


# def second_num(n):
#     if n > 0:
#         print(math.floor(n * 100) % 10)
#     else:
#         print('Number must be more than zero!')
#
#
# number = float(input('Enter the number: '))
# second_num(number)


# x = float(input('Enter the X: '))
# y = float(input('Enter the Y: '))
# distance = math.sqrt(x ** 2 + y ** 2)
# space = math.sqrt(1 ** 2 + 1 ** 2)
# if distance > space:
#     print('There is not coin at the area')
# else:
#     print('The coin is nearby!')


# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# min_n = (abs(num1 - num2) - (num1 + num2)) // 2
# print(abs(min_n))


# import math
# def gcb(a, b):
#     while a != 0 and b != 0:
#         # сравнивать их между собой.
#         # Если первое число больше второго,
#         if a > b:
#             # то находить остаток от деления его на второе число
#             # и присваивать его первой переменной
#             a = a % b
#         # Иначе (когда второе число больше первого)
#         else:
#             # присваивать второй переменной остаток от деления
#             # нацело второго числа на первое
#             b = b % a
#     # Одно из чисел содержит 0, а другое - НОД, но какое - неизвестно.
#     # Проще их сложить, чем писать конструкцию if-else
#     gcd = a + b
#     print(gcd)
#
#
# a, b = int(input('Введите число a: ')), int(input('Введите число b: '))
# gcb(a, b)
# # =
# print(math.gcd(a, b))


# def coin_count(one, five, ten, fifty):
#     one *= 0.01
#     five *= 0.05
#     ten *= 0.1
#     fifty *= 0.5
#     summ = one + five + ten + fifty
#     print(round(summ, 2))
#
# coin_count(3, 6, 7, 2)


# def rock_paper_scissors():
#     user_move = input('\nRock, scissors or paper? ')
#     if user_move == 'scissors':
#         print('You won!')
#     elif user_move == 'rock':
#         print('You lose!')
#     else:
#         print('It is a draw\n')
#     mainMenu()
#
#
# def guess_the_number():
#     number = int(input('\nEnter the number: '))
#     while number != 7:
#         print('\nWrong number! Try again!')
#         number = int(input('Enter the number: '))
#     print('You won!\n')
#     mainMenu()
#
#
# def mainMenu():
#     print("What kind game do you wanna play?\n1 - rock, paper, scissors\n2 - guess the number")
#     answer = int(input())
#     if answer == 1:
#         rock_paper_scissors()
#     elif answer == 2:
#         guess_the_number()
#     else:
#         mainMenu()
#
#
# mainMenu()


# def funct(n):
#     print(n, end='')
#     num = n
#     if num >= 3:
#         num //= 2
#         if num != 1:
#             print(num, end='')
#         else:
#             pass
#         if num >= 3:
#             num //= 2
#             if num != 1:
#                 print(num, end='')
#             else:
#                 pass
#         if n >= 5:
#             n -= 1
#             funct(n)
#
#
# number = int(input('Enter the number: '))
# funct(number)