# Task 1. Songs 2
#
# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
#
# total_sound = []
# take_songs = int(input('How many songs to choose? '))
# for _ in range(take_songs):
#     name = input('Enter name of song: ')
#     total_sound.append(violator_songs.get(name, 0))
#
# print(f"\nTotal time sounding: {sum(total_sound)}")


# Task 2. Geography
#
# def find_country(num_countr):
#     dict_country = dict()
#     list_country = input('').split()
#     country = list_country[0]
#     list_country.remove(list_country[0])
#     for city in list_country:
#         dict_country[city] = country
#     return dict_country
#
#
# number_countries = int(input('Enter number of countries: '))
#
# total_dict = dict()
# for i in range(1, number_countries + 1):
#     print(f"{i} country:", end='')
#     total_dict.update(find_country(number_countries))
#
# for j in range(1, 4):
#     print(f"\n{j} city:", end='')
#     city_name = input('')
#     if total_dict.get(city_name):
#         print(f"{city_name} city is a part of {total_dict.get(city_name)}")
#     else:
#         print(total_dict.get(city_name, f"No info about {city_name}"))

