# Task 1. Passport data
#
# def find_name_surname(ser, num, dictionary):
#     for key, value in dictionary.items():
#         if ser and num in key:
#             name_f = value[0]
#             surname_f = value[1]
#     return name_f, surname_f
#
#
# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
#
# series = int(input('Enter series of the passport: '))
# number = int(input('Enter number of the passport: '))
#
# surname, name = find_name_surname(series, number, data)
# print(name, surname)


# Task 2. Contacts 2
#
#
# phone_book = dict()
#
# while True:
#     print('Current contacts on the phone book:')
#     if phone_book:
#         for key, val in phone_book.items():
#             for i_key, i_val in enumerate(key):
#                 print(i_val, end=' ')
#             else:
#                 print('--- {v}'.format(v=val))
#     else:
#         print('<Clear>')
#
#     contact_name = tuple(input('\nEnter new contact (name surname): ').split())
#     phone_number = int(input('Enter phone number: '))
#     phone_book[contact_name] = phone_number
