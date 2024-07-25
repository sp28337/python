# Task 1. Star Wars
# import json
# import pprint
# import requests
#
# my_req = requests.get('https://swapi.dev/api/planets/3/')
# data = json.loads(my_req.text)
# pprint.pprint(data)
# data['name'] = 'Pavel Tarakanov'
#
# with open('my_test2.json', 'w') as file:
#     json.dump(data, file, indent=4)
#
# print('=' * 70)
#
# print(data['films'])
#
# films_req = requests.get(data['films'][0])
# films = json.loads(films_req.text)
# pprint.pprint(films)
