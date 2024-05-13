import math

# price_eu = float(input('What is the price in euro? '))
# price_us = price_eu * 1.25
# price_ru = price_us * 60.87
# print(round(price_ru, 2))


# pressure_zero = float(input('What is the pressure at zero degrees? '))
# temperature = float(input('What is the temperature? '))
# pressure = (pressure_zero * (273 + temperature)) / 273
# print(f"Pressure that we are seeking for is {round(pressure, 2)}")


# numbers = int(input('Enter how much numbers will be: '))
# for i in range(numbers):
#     n = float(input('Enter the number: '))
#     if n < 0:
#         n = math.floor(n)
#         print(f"x = {n} log(x) = {math.exp(n)}")
#     else:
#         n = math.ceil(n)
#         print(f"x = {n} log(x) = {math.log(n)}")


# message = input('Enter the message: ')
# bits = math.ceil(math.log(len(message), 2))
# if math.ceil(math.log2(len(message))) != bits:
#     print('error!')
# elif len(message) == 1:
#     print(f"There are 1 symbols. Minimal bits: 1")
# else:
#     print(f"There are {len(message)} symbols. Minimal bits: {bits}")


# file_size = int(input("Specify the file size to download: "))
# connection_speed = int(input('What is your connection speed? '))
# downloaded, seconds = 0, 0
# while downloaded < file_size:
#     seconds += 1
#     downloaded += connection_speed
#     if downloaded > file_size:
#         downloaded = file_size
#     percent = (100 * downloaded) / file_size
#     print(f"{seconds} second(s) has passed. Downloaded {downloaded} MB of {file_size} ({math.ceil(percent)}%)")


# x = float(input('Enter the number: '))
# print(math.floor(x * 10))


# radius = float(input('Enter radius of the planet: '))
# earth_v = round(10.8321 * 10 ** 11)
# v = (4 / 3) * math.pi * (radius ** 3)
# if earth_v > v:
#     print(f"The volume of planet Earth is {round(earth_v / v, 3)} times greater")
# else:
#     print(f"The volume of planet Earth is {round(v / earth_v, 3)} times smaller")


# lower_t = int(input('Enter lower temperature limit: '))
# upper_t = int(input('Enter upper temperature limit: '))
# step = int(input('Enter step: '))
# print('C    F')
# for i in range(lower_t, upper_t + 1, step):
#     f = 32
#     print(f"{i:<3} {f + int(math.ceil(i * 1.8)):^3}")
# else:
#     if i != upper_t:
#         print(f"{upper_t:^3} {f + int(math.ceil(upper_t * 1.8)):^3}")


# print('Enter cube size: ')
# x = float(input('X: '))
# y = float(input('Y: '))
# z = float(input('Z: '))
# s = math.floor(y) * math.floor(z)
# print(f"You can make {int((s / 5) / 5)} cubes from the wood")
# print(f"From these you can organize a set of {int(((s / 5) / 5) // 8)} cubes")


# pitch_angle = float(input('Enter pitch angle: '))
# while abs(pitch_angle) > 360:
#         pitch_angle -= 360
# print(pitch_angle)
# in_radians = round(pitch_angle / 57.2958, 2)
# if -0.28 <= in_radians <= 0.28:
#     print(f"Angle is safe! {in_radians}")
# else:
#     print('Danger angle!', in_radians)


# print("Enter the horse's location: ")
# y = float(input())
# x = float(input())
# print("Enter the point location: ")
# y2 = float(input())
# x2 = float(input())
# y = int(y * 10)
# x = int(x * 10)
# y2 = int(y2 * 10)
# x2 = int(x2 * 10)
# print(f"The horse is at ({y}, {x}) cell")
# print(f"The point is at ({y2}, {x2}) cell")
# if abs((y - y2) * (x - x2)) == 2:
#     print('Yes')
# else:
#     print('No')


# hours = int(input('Enter hours '))
# minutes = int(input('Enter minutes: '))
# seconds = int(input('Enter seconds: '))
# angle_h = (hours * 3600 + minutes * 60 + seconds) / 120
# angle_m = (minutes * 60 + seconds) / 10
# print("The hour hand has turned to", round(angle_h, 2))
# print("The minute hand has turned to", round(angle_m, 2))
#
# angle = float(input('Enter the angle by which the hour hand rotates: '))
# minute_arrow_angle = (angle * 12) % 360
# print(f"After the last hour the minute hand has turned to {round(minute_arrow_angle, 2)} degrees")


# a, b, c = float(input('a = ')), float(input('b = ')), float(input('c = '))
# d = b ** 2 - 4 * a * c
# if d < 0:
#     print('There are not roots')
# elif d > 0:
#     x1 = (-b + math.sqrt(d)) / (2 * a)
#     x2 = (-b - math.sqrt(d)) / (2 * a)
#     print(f'There are two roots:\n1) {x1}\n2) {x2}')
# else:
#     x = -(b / (2 * a))
#     print('There are one root:', x)


# n1 = int(input('Enter the number 1: '))
# n2 = int(input('Enter the number 2: '))
# max_n = ((n1 + n2) + abs(n1 - n2)) / 2
# print(int(max_n))

