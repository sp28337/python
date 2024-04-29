# def greeting():
#     while True:
#         a = input('Зайдёте? Да/Нет: ')
#         if a == 'Да':
#             print('Привет!')
#             print('Добро пожаловать!')
#         print('Следующий.')
#         greeting()
#
#
# greeting()


# def summ():
#     a = int(input())
#     b = int(input())
#     summa = a + b
#     print("Всего", a + b, "шт.")
#
#
# print("Сколько мешков рыбы и мяса?")
# summ()
# print("Сколько буханок белого и чёрного хлеба?")
# summ()
# print("Сколько вёдер воды и молока?")
# summ()


# def name():
#     print('Surname: Ivanov')
#     print('Name: Vasiliy')
#     print('Street: Pushkina')
#     print('Home: 32\n')
#
# name()
# name()
# name()


# def triangle():
#     for i in range(1, 5 + 1):
#         print(' ' * (5 - i) + '*' * (i * 2 - 1))
#
#
# def rectangle():
#     for i in range(1, 5 + 1):
#         if i == 1 or i == 5:
#             print('|' + '-' * 10 + '|')
#         else:
#             print('|' + ' ' * 10 + '|')
#
#
# paint = input('What do you wanna draw? ')
# if paint == 'rectangle':
#     rectangle()
# elif paint == 'triangle':
#     triangle()
