# Task 1. Work with file
#
# def what_to_do(question,
#                error='Wrong input. Please enter <yes> or <no>.',
#                retries=5):
#     while True:
#         answer = input(question).lower()
#         if answer == 'yes':
#             return 1
#         elif answer == 'no':
#             return 0
#         retries -= 1
#         if retries == 0:
#             break
#         print(error)
#         print('Last retries:', retries)
#
#
# what_to_do('Do you really wanna go out?')
# what_to_do('Do you wanna delete file?', 'So delete or not?')
# what_to_do('Write a file?', retries=2)
