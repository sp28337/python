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


# Task 3. Krypto
#
# data = {
#     "address": "0x544444444444",
#     "ETH": {
#         "balance": 444,
#         "totalIn": 444,
#         "totalOut": 4
#     },
#     "count_txs": 2,
#     "tokens": [
#         {
#             "fst_token_info": {
#                 "address": "0x44444",
#                 "name": "fdf",
#                 "decimals": 0,
#                 "symbol": "dsfdsf",
#                 "total_supply": "3228562189",
#                 "owner": "0x44444",
#                 "last_updated": 1519022607901,
#                 "issuances_count": 0,
#                 "holders_count": 137528,
#                 "price": False
#             },
#             "balance": 5000,
#             "totalIn": 0,
#             "totalOut": 0
#         },
#         {
#             "sec_token_info": {
#                 "address": "0x44444",
#                 "name": "ggg",
#                 "decimals": "2",
#                 "symbol": "fff",
#                 "total_supply": "250000000000",
#                 "owner": "0x44444",
#                 "last_updated": 1520452201,
#                 "issuances_count": 0,
#                 "holders_count": 20707,
#                 "price": False
#             },
#             "balance": 500,
#             "totalIn": 0,
#             "total_out": 0
#         }
#     ]
# }
#
#
# for key in data:
#     print(key, ':', data[key])
#
# data['ETH'].setdefault('total_diff', 100)
# data['tokens'][0]['fst_token_info']['name'] = 'doge'
# data['ETH']['totalOut'] = data['tokens'][0]['totalOut']
# del data['tokens'][0]['totalOut']
# data["tokens"][1]["sec_token_info"].keys()
# value = data["tokens"][1]["sec_token_info"].pop('price')
# data["tokens"][1]["sec_token_info"]['total_price'] = value
# print(data["tokens"][1]["sec_token_info"])


# Task 4. Goods
#
# def total_summ_and_profit(list_items):
#     total_sum = total_profit = 0
#     for i in list_items:
#         total_sum += i['quantity']
#         total_profit += i['price'] * i['quantity']
#     print(total_sum, 'шт, стоимость', total_profit, 'руб')
#
# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
#
# for item in goods.keys():
#     print(item, '-', end=' ')
#     for i_store in store.keys():
#         if goods[item] == i_store:
#             total_summ_and_profit(store[i_store])


# Task 5. Histogramm 2
#
# def inversion(dictionary):
#     rev_dict = dict()
#     new_set = set(x for x in dictionary.values())
#     for key in new_set:
#         value = [x for x in dictionary.keys() if dictionary[x] == key]
#         rev_dict[key] = value
#     return rev_dict
#
#
# text = (input('Enter the text: '))
# dict_hist = {x: text.count(x) for x in sorted(text)}
#
# print('Original dict of hists:')
# for i in dict_hist.keys():
#     print(i, ':', dict_hist[i])
#
# print('\nInverted dict of hists:')
#
# invert_dict = inversion(dict_hist)
# for j in invert_dict:
#     print(j, ':', invert_dict[j])


# Task 6. Synonyms dict
#
# amount_pairs = int(input('Enter the number of word pairs: '))
# synonyms_dict = dict()
# for pair in range(1, amount_pairs + 1):
#     print(f"{pair} pair:", end='')
#     words_pair = ''.join(input('').title().split())
#     synonyms_dict.setdefault(words_pair[:words_pair.index('-')], words_pair[words_pair.index('-') + 1:])
#
# print(synonyms_dict)
# flag = True
# while flag:
#     word = input('Enter the word: ').title()
#     for key, value in synonyms_dict.items():
#         if word == key:
#             print(value)
#             flag = False
#             break
#         elif word == value:
#             print(key)
#             flag = False
#             break
#     else:
#         print('There is not word like this in the dictionary.')

