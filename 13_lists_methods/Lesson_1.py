# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1, 'bear')
# zoo.remove('elephant')
# print(zoo)
# print('Lion in a cage number:', zoo.index('lion') + 1)
# print('Monkey in a cage number:', zoo.index('monkey') + 1)


# def del_zero(list_fix):
#     for i in list_fix:
#         if i == 0:
#             list_fix.remove(i)
#     return list_fix
#
#
# salary_log = []
# employees = int(input('Count of employees: '))
# for i in range(1, employees + 1):
#     print(f"Salary of {i} employee:", end=' ')
#     salary = int(input())
#     salary_log.append(salary)
#
# del_zero(salary_log)
#
# print(f"Last employees: {len(salary_log)}")
# print('Salaries:', salary_log)
# print('Max salary:', max(salary_log))
# print('Min salary:', min(salary_log))


# def is_movie_in_list(film, movie_list):
#     if film in movie_list:
#         return True
#     return False
#
#
# films = ['Taxi', 'Leon', 'Village', 'Matrix', 'Titanic', 'Terminator', 'Never give up', 'Interstellar', 'Forest Gump']
# favorite = []
#
# while True:
#     print(f"Your TOP movie: {favorite}\n")
#     movie = input('Movie: ')
#     if is_movie_in_list(movie, films):
#         print("Commands: ADD, PASTE, RM")
#         command = input('Enter command: ')
#         if command == 'ADD':
#             if is_movie_in_list(movie, favorite):
#                 print('This movie already exists in your favorites.')
#                 continue
#             else:
#                 favorite.append(movie)
#         elif command == 'PASTE':
#             if is_movie_in_list(movie, favorite):
#                 print('This movie already exists in your favorites.')
#                 continue
#             else:
#                 index = int(input('Enter index for paste: '))
#                 favorite.insert(index - 1, movie)
#
#         elif command == 'RM':
#             if is_movie_in_list(movie, favorite):
#                 favorite.remove(movie)
#             else:
#                 print('There are not film like that in your favorites.')
#         print()
#     else:
#         print('There are not movie lake that in our platform.')