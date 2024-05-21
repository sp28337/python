# Task 1. Crisis is over
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for fruit_name, estimate in incomes.items():
#     print('{fruit} -- {price}'.format(fruit=fruit_name, price=estimate))


# Task 2. Server
#
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
# for i_key, i_value in server_data.items():
#     print('{key}:'.format(key=i_key))
#     for j_key, j_value in i_value.items():
#         print('    {key}: {value}'.format(key=j_key, value=j_value))
#     print()


# Task 3. In a string
#
# print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])
