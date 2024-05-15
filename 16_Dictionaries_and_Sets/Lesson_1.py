# Task 1. Dict squares
#
# num = int(input('Enter number: '))
# new_dict = dict()
# for key in range(1, num + 1):
#     new_dict[key] = key ** 2
#
# print(new_dict)


# Task 2. Student
#
# student_info = input('Enter info of student separated by spaces(name, surname, city, study place, grates): ').split()
# student = dict()
# student['Name'] = student_info[0]
# student['Surname'] = student_info[1]
# student['City'] = student_info[2]
# student['Study place'] = student_info[3]
# student['Grates'] = []
# for i_grates in student_info[-4:]:
#     student['Grates'].append(i_grates)
# for i in student:
#     print(i, '-', student[i])


# Task 3. Contacts
#
# phone_book = dict()
# while True:
#     print('Current contacts on the phone book:')
#     if phone_book:
#         for i in phone_book:
#             print(i, phone_book[i])
#     else:
#         print('<Clear>')
#     contact_name = input('Enter contact name: ')
#     if contact_name in phone_book:
#         print('Error: this name already exist in the dictionary!')
#
#     else:
#         phone_number = int(input('Enter phone number: '))
#         phone_book[contact_name] = phone_number
#     print()
