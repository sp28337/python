# Task 1. Lorem ipsum
# import re
#
#
# text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
# Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
# nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
# Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate
# """
#
# fou_letters_word = re.findall(r"\b\w{4}\b", text)
# print(fou_letters_word)


# Task 2. Registration plates
# import re
#
#
# reg_plates = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
# pattern1 = r"\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d+\b"
# pattern2 = r"\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b"
#
# private_vehicles = re.findall(pattern1, reg_plates)
# taxi = re.findall(pattern2, reg_plates)
#
# print(*private_vehicles)
# print(*taxi)


# Task 3. Breaking bad
# pass


# Task 4. Phone numbers
# import re
#
#
# numbers = ['9999999999', '999999-999', '99999x9999']
# pattern = r"\b[8-9]\d{9}\b"
#
# for number in numbers:
#     if re.findall(pattern, number):
#         print('OK')
#     else:
#         print('NOT')